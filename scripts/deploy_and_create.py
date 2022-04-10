from scripts.helpful_scripts import OPENSEA_FORMAT, get_account
from brownie import SimpleCollectibles

sample_token_uri= "ipfs://Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"
def main():
    account = get_account()
    simple_collectible = SimpleCollectibles.deploy( {"from":account})
    tx = simple_collectible.createCollectible(sample_token_uri, {"from":account})
    tx.wait(1)
    print(f"awesome, you can view your NFT at  {OPENSEA_URL.format(simple_collectible.address, simple_collectible.tokenCounter()-1)}")