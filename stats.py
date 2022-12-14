
from utils.args import parse_args
from ghcl.contributions import Contributions
from ghcl.github_stats import GithubStats

args = parse_args()
contribs = Contributions(GithubStats(access_token=args['access_token']))
stats = contribs.leaderboard(
    args['users'], args['start_date'], args['end_date'])

for stat in stats:
    print(getattr(stat, f"{args['mode']}_data")())
