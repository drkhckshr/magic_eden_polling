# Magic Eden Polling

## Requirements

* Docker
  * [Get Docker Desktop](https://www.docker.com/products/docker-desktop)

## Quick Start

Clone this repo

```
git clone ....
```

Build the Docker image

```
cd magic_eden_polling
docker build --tag mepoll .
```

Run the container

```
cd mepoll
docker run --rm  -v `pwd`:/tmp -it mepoll python tmp/src/get_me_nfts.py
```

To modify what NFTs to target update the `me_nfts.json` file.

The only requirement is to begin is to have the `.json` in the following format.

```
[
    {"url": "https://api-mainnet.magiceden.io/rpc/getNFTByMintAddress/<mint_address_for_the_nft>"}
]
```

To poll multiple NFTs add more to the array/list like so

```
[
    {"url": "https://api-mainnet.magiceden.io/rpc/getNFTByMintAddress/<mint_address_for_the_nft>"},
    {"url": "https://api-mainnet.magiceden.io/rpc/getNFTByMintAddress/<mint_address_for_another_nft>"}
]
```

The mint address is easy to find. Just select the NFT from Magic Eden and look at the URL in your browser. It will be the random character portion of the URL after `item-details`. 
```
https://magiceden.io/item-details/2t2EAthJUJtTTvbDk9r72evvmGspQ9C1gmedKUCnjVNN
```
