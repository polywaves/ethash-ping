import requests
from settings import envs


def get_bc_data():
    res = requests.get(envs['BLOCKCYPHER_URL'])
    keys = res.json()
    return keys['height'], res.elapsed.total_seconds()


def get_es_data():
    res = requests.get(envs['ETHERSCAN_URL'])
    keys = res.json()
    return keys['result'], res.elapsed.total_seconds()


def main():
    bc_height, bc_elapsed = get_bc_data()
    es_result, es_elapsed = get_es_data()

    print(f'Blockcypher height: {bc_height}')
    print(f'Etherscan result: {es_result}')

    print(f'Blockcypher elapsed: {bc_elapsed}')
    print(f'Etherscan elapsed: {es_elapsed}')


if __name__ == '__main__':
    main()
