
import os
import botocore
import botocore.session
import json
import sys


from aws_secretsmanager_caching import SecretCache, SecretCacheConfig
from botocore.config import Config

client = botocore.session.get_session().create_client('secretsmanager')
cache_config = SecretCacheConfig()
cache = SecretCache( config = cache_config, client = client)

path = sys.argv[1]
prefix = sys.argv[2]
public = sys.argv[3].split()
private = sys.argv[4].split()
file = sys.argv[5].split()


secret = json.loads(cache.get_secret_string(path))


with open(os.environ['GITHUB_ENV'], "a") as env_file:
    for name in public:
        env_file.write(f'{ prefix.upper() }_{ name.upper() }={ secret[name] }\n')
    for name in private:
        env_file.write(f'{ prefix.upper() }_{ name.upper() }={ secret[name] }\n')
        print(f"::add-mask::{ secret[name] }")

for name in file:
    with open(f'{ prefix.lower() }_{ name.lower() }', "w") as secret_file:
        secret_file.write(secret[name])
