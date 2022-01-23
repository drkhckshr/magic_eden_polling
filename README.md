# Magic Eden Polling

## Requirements

* Docker
  * [Get Docker Desktop](https://www.docker.com/products/docker-desktop)

The `Dockerfile` will take care of the rest of the dependencies.

## Quick Start

Clone this repo

```
git clone https://github.com/drkhckshr/magic_eden_polling.git
```

Build the Docker image

```
cd magic_eden_polling
docker build --tag mepoll .
```

Run the container

```
cd mepoll
docker run --rm  -v `pwd`:/tmp -it mepoll python tmp/src/get_me_nft_collections.py
```

## Usage

To modify what NFT collections to target update the `me_nft_collections.json` file in `mepoll/files`.

The only requirement is to begin is to have the `.json` in the following format.

```
[
    {
        "collectionName": "skeleton_crew_skulls"
    },
    {
        "collectionName": "skeleton_crew_airdrops_and_more"
    }
]
```

You can find the collection name in your browser's address bar. 

For example, the `Skeleton Crew Skulls` collection is at

```
https://www.magiceden.io/marketplace/skeleton_crew_skulls
```

In `mepoll/files` you see additional `.json` files with the most recently listed NFTs in each collection.

Each `.json` collection file will follow the naming convention of `me_nft_<collection_name>.json`.

## Support

Please open an issue in this repository if you are having trouble or need assistance.

## Contributions

Pull requests are welcomed and encouraged! 

If you find this repository useful and would rather contribute defi-nancially tips are appreciated.

You can send $SOL to `drkhckshr.sol` in a [Phantom wallet](https://phantom.app/) or to the following wallet address:
* `JD8dLRk7YHBaekkGftdKUbQB1hc3jLwJ87e8zJUiqR6s`