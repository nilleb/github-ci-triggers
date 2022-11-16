import argparse
from jira import JIRA


def parse_args():
    parser = argparse.ArgumentParser(
        description="transition jira issue to the given state"
    )

    parser.add_argument("--server", dest="server")
    parser.add_argument("--email", dest="email")
    parser.add_argument("--token", dest="token")
    parser.add_argument("issue_id")
    parser.add_argument("to_state")
    parser.add_argument("--timespent", dest="time_spent", default="2h")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    jira = JIRA(server=args.server, basic_auth=(args.email, args.token))
    issue = jira.issue(args.issue_id)

    jira.transition_issue(args.issue_id, args.to_state, worklog="2h")
