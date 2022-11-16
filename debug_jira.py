import argparse
from jira import JIRA

def view_transitions(jira, issue):
    transitions = jira.transitions(issue)
    print([(t['id'], t['name']) for t in transitions])

def view_states(jira, issue):
    fields_definitions = {field["id"]: field for field in jira.fields()}
    for field_name in issue.raw['fields']:
        fdef = fields_definitions[field_name]
        print("Field:", field_name, "Value:", issue.raw['fields'][field_name], "Definition: ", fdef)

    print(issue.raw['fields']['timespent'])
    print(issue.raw['fields']['timetracking'])

def update_timespent(issue_id: str, elapsed_time: str = '2h'):
    # not the right way to set the timespent
    # issue.update(fields={'timespent': '1h'})
    # the right way to add a time spent
    jira.add_worklog(issue_id, timeSpent=elapsed_time)

def parse_args():
    parser = argparse.ArgumentParser(
        description="inspect jira issue transitions and fields"
    )

    parser.add_argument("--server", dest="server")
    parser.add_argument("--email", dest="email")
    parser.add_argument("--token", dest="token")
    parser.add_argument("issue_id")
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()

    jira = JIRA(server=args.server, basic_auth=(args.email, args.token))
    issue = jira.issue(args.issue_id)

    view_transitions(jira, issue)
    # documentation: all the available transitions
    # [('791', 'Verified'), ('821', 'Resolved'), ('841', 'In Progress (2)'), ('851', 'To review'), ('871', 'To Fix'), ('881', 'Closed'), ('891', 'Open'), ('901', 'Archived')]
    view_states(jira, issue)

    # To Verify = Resolved
    # jira.transition_issue(issue_id, 'Resolved', worklog='2h')
    # jira.transition_issue(issue_id, 'To fix', worklog='0m')
