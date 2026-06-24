import random
import subprocess
from datetime import datetime, timedelta

ACTIONS = ["Refactored", "Fixed", "Updated", "Optimized", "Added", "Cleaned", "Improved", "Reviewed"]
TERMS = ["auth", "user", "payment", "cache", "api", "config", "logger", "scheduler", "database", "middleware"]
SUFFIXES = ["module", "handler", "service", "endpoint", "logic", "tests", "query", "imports"]
PREFIXES = {
    "Refactored": "refactor", "Fixed": "fix", "Updated": "chore",
    "Optimized": "perf", "Added": "feat", "Cleaned": "chore",
    "Improved": "refactor", "Reviewed": "chore",
}

count = random.randint(30, 50)
t = datetime.utcnow().replace(hour=9, minute=0, second=0, microsecond=0)

for _ in range(count):
    action = random.choice(ACTIONS)
    term = random.choice(TERMS)
    suffix = random.choice(SUFFIXES)
    msg = f"{PREFIXES[action]}: {term} {suffix} update"

    with open("dev-log.md", "a") as f:
        f.write(f"[{t.strftime('%Y-%m-%d %H:%M')}] {action} {term} {suffix}\n")

    subprocess.run(["git", "add", "dev-log.md"], check=True)
    subprocess.run(["git", "commit", "-m", msg], check=True)

    t += timedelta(minutes=random.randint(20, 90))
    if t.hour > 22:
        t = t.replace(hour=22, minute=0)

print(f"Done: {count} commits")
