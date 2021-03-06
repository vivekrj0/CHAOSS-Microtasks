import configparser
import requests
import json
import sys

def mordred(organisation_name):
    config = configparser.ConfigParser()
    config.add_section('general')
    config['general']['short_name'] = organisation_name
    config['general']['update'] = 'false'
    config['general']['sleep'] = '0'
    config['general']['debug'] = 'true'
    config['general']['min_update_delay'] = '10'
    config['general']['logs_dir'] = '/tmp/logs'
    config['general']['kibana'] = '"5"'

    config.add_section('projects')
    config['projects']['projects_file'] = organisation_name + '.json'

    config.add_section('es_collection')
    ecollect = config['es_collection']
    ecollect['url'] = 'http://localhost:9200'
    ecollect['user'] = ''
    ecollect['password'] = ''

    config.add_section('es_enrichment')
    enrich = config['es_enrichment']
    enrich['url'] = 'http://127.0.0.1:9200'
    enrich['user'] = ''
    enrich['password'] = ''
    enrich['autorefresh'] = 'false'

    config.add_section('sortinghat')
    st = config['sortinghat']
    st['host'] = 'localhost'
    st['user'] = 'user'
    st['password'] = 'XXX'
    st['database'] = 'database'
    st['load_orgs'] = 'false'
    st['unify_method'] = ''
    st['unaffiliated_group'] = 'Unknown'
    st['affiliate'] = 'True'
    st['autoprofile'] = '[customer,git,github]'
    st['matching'] = '[email]'
    st['sleep_for'] = '0'
    st['bots_names'] = '[Beloved Bot]'

    config.add_section('panels')
    config['panels']['kibiter_time_from'] = '"now-90d"'

    config.add_section('phases')
    config['phases']['collection'] = 'true'
    config['phases']['identities'] = 'true'
    config['phases']['enrichment'] = 'true'
    config['phases']['panels'] = 'true'

    config.add_section('git')
    config['git']['raw_index'] = 'git_test-raw'
    config['git']['enriched_index'] = 'git_test'

    config.add_section('github')
    config['github']['api-token'] = 'Your API-Token'
    config['github']['raw_index'] = 'github_test-raw'
    config['github']['enriched_index'] = 'github_test'

    return config


def projects(organisation_name):
    organisation_url = "https://api.github.com/users/" + organisation_name + "/repos"
    git_url = []
    github_url = []

    r = requests.get(organisation_url + "?page=0")

    while ('next' in r.links or not r.links):
        for repo in r.json():
            if not repo['fork']:
                git_url.append(repo['clone_url'])
                github_url.append(repo['html_url'])
        if not r.links:
            break
        r = requests.get(r.links['next']['url'])

    json_new = {}
    json_new[organisation_name] = {}
    json_new[organisation_name]['git'] = git_url 
    json_new[organisation_name]['github'] = github_url

    
    with open(organisation_name + ".json", "w") as new:
        json.dump(json_new, new)

def main():
    if len(sys.argv) >= 3:
        sys.stderr.write("Enter Organisation Name at terminal")
        sys.exit(1)
    organisation_name = sys.argv[1]

    mordred_file = mordred(organisation_name)
    projects(organisation_name)
   
    with open(organisation_name + ".cfg", "w") as new:
        mordred_file.write(new)

    return 0

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        sys.exit(1)
