import os
import re
from datetime import datetime

# Define the expanded category mapping
category_mapping = {
    # Layer 1 (Base Chains)
    'Avalanche': ['layer-1', 'blockchain'],
    'Aptos': ['layer-1', 'blockchain', 'move'],
    'Internet Computer': ['layer-1', 'blockchain'],
    'Polkadot': ['layer-1', 'blockchain'],
    'Celestia': ['layer-1', 'blockchain', 'modular'],
    'Sei': ['layer-1', 'blockchain', 'trading'],
    'Mode': ['layer-1', 'blockchain'],
    'Saga': ['layer-1', 'blockchain'],
    'Dymension': ['layer-1', 'rollup'],
    'Archway': ['layer-1', 'blockchain', 'cosmos'],
    'Namada': ['layer-1', 'blockchain', 'privacy'],

    # Layer 2 (Scaling Solutions)
    'zkSync': ['layer-2', 'scaling', 'ethereum'],
    'Scroll': ['layer-2', 'scaling', 'ethereum'],
    'Taiko': ['layer-2', 'scaling', 'ethereum'],
    'Arbitrum': ['layer-2', 'scaling', 'ethereum'],
    'Optimism': ['layer-2', 'scaling', 'ethereum'],
    'zkFair': ['layer-2', 'scaling'],
    'AltLayer': ['layer-2', 'infrastructure'],
    'Starknet': ['layer-2', 'scaling', 'ethereum'],
    'Polygon-zkEVM': ['layer-2', 'scaling', 'ethereum'],
    'Layer3': ['infrastructure', 'scaling', 'blockchain'],
    'Lumoz': ['infrastructure', 'scaling', 'layer-2'],
    'Soarchain': ['infrastructure', 'scaling', 'performance'],
    'Fuel-Network': ['infrastructure', 'layer-2', 'ethereum'],
    'Zircuit': ['infrastructure', 'zk-rollup', 'privacy'],
    'zkLink': ['infrastructure', 'cross-chain', 'zk-rollup'],

    # Infrastructure
    'LayerZero': ['infrastructure', 'cross-chain'],
    'Kontos': ['infrastructure', 'finance', 'accounting'],
    'Thruster': ['infrastructure', 'performance', 'development'],
    'Spectral-Labs': ['infrastructure', 'analytics', 'visualization'],
    'Ora-Protocol': ['infrastructure', 'oracles', 'data'],
    'Nois-Randdrop': ['infrastructure', 'randomness', 'security'],
    'Genisos-Safe': ['infrastructure', 'security', 'defi'],
    'Anzen': ['infrastructure', 'security', 'safety'],
    'Lava': ['infrastructure', 'data', 'energy'],
    'Port3': ['infrastructure', 'logistics', 'data'],
    'Seamless': ['infrastructure', 'usability', 'blockchain'],
    'Jito': ['infrastructure', 'mev', 'solana'],
    'Orchai': ['infrastructure', 'automation', 'integration'],
    'DappRadar': ['infrastructure', 'analytics', 'dapps'],
    'Genie': ['infrastructure', 'automation', 'blockchain'],
    'Tornado-Cash': ['infrastructure', 'privacy', 'ethereum'],
    'Biconomy': ['infrastructure', 'usability', 'defi'],
    'DeepBook': ['infrastructure', 'dex', 'order-book'],
    'Pontem-Network': ['infrastructure', 'move', 'blockchain'],
    'Arkham': ['infrastructure', 'data', 'analytics'],
    'AVAV': ['infrastructure', 'token', 'utility'],
    'Unlock-Protocol': ['infrastructure', 'access', 'control'],

    # Bridges/Cross-chain
    'deBridge': ['infrastructure', 'bridge', 'cross-chain'],
    'Axelar-Network': ['infrastructure', 'cross-chain'],
    'Wormhole': ['infrastructure', 'cross-chain'],
    'ZetaChain': ['infrastructure', 'cross-chain'],
    'Portal': ['infrastructure', 'cross-chain'],
    'Kima-Network': ['infrastructure', 'payments', 'cross-chain'],
    'Hop-Protocol': ['infrastructure', 'cross-chain', 'transfer'],
    'Across-Protocol': ['infrastructure', 'cross-chain', 'liquidity'],

    # Wallets
    'Sender-Wallet': ['infrastructure', 'wallet'],
    'WalletConnect': ['infrastructure', 'wallet', 'protocol'],
    'Holdstation': ['infrastructure', 'wallet'],
    'Safe': ['infrastructure', 'multisig', 'wallet'],

    # Oracles and Data
    'Pyth-Network': ['infrastructure', 'oracle'],
    'Graph-Protocol': ['infrastructure', 'indexing'],
    'Vana': ['data', 'marketplace', 'privacy'],

    # DeFi - DEX
    '1inch': ['defi', 'dex', 'protocol'],
    'Uniswap': ['defi', 'dex', 'protocol'],
    'Curve': ['defi', 'dex', 'stablecoin'],
    'CowSwap': ['defi', 'dex', 'aggregator'],
    'Velodrome-Finance': ['defi', 'dex', 'optimism'],
    'Jupiter': ['defi', 'dex', 'aggregator', 'solana'],
    'SpartaDEX': ['defi', 'dex'],
    'Virtuswap': ['defi', 'dex'],
    'ZigZag-Exchange': ['defi', 'dex'],
    'Diffusion-Finance': ['defi', 'dex'],
    'Odos-Protocol': ['defi', 'dex', 'aggregator'],
    'Thena': ['defi', 'dex'],
    'Paraswap': ['defi', 'dex', 'aggregator'],
    'Sudoswap': ['defi', 'dex', 'nft'],
    'Animeswap': ['defi', 'dex'],
    'Arbswap': ['defi', 'dex', 'arbitrum'],
    'Hashflow': ['defi', 'dex', 'cross-chain'],
    'Osmosis': ['defi', 'dex', 'cosmos'],
    'DFYN': ['defi', 'dex', 'cross-chain'],

    # DeFi - Lending
    'Compound': ['defi', 'lending', 'protocol'],
    'Morpho-Labs': ['defi', 'lending', 'optimization'],
    'Exactly-Protocol': ['defi', 'lending'],
    'Granary': ['defi', 'lending'],
    'Inverse-Finance': ['defi', 'lending', 'synthetics'],
    'Gearbox': ['defi', 'lending'],
    'Raft': ['defi', 'lending', 'stablecoin'],
    'Sturdy-Finance': ['defi', 'lending', 'risk-management'],
    'Goldfinch-fi': ['defi', 'lending', 'business'],
    'Zeus': ['defi', 'lending', 'insurance'],
    'Lifeform': ['defi', 'lending', 'borrowing'],

    # DeFi - Trading/Perpetuals
    'dYdX': ['defi', 'perpetuals', 'trading'],
    'Drift': ['defi', 'perpetuals'],
    'ZKX': ['defi', 'derivatives', 'trading'],
    'Vela-Exchange': ['defi', 'trading'],
    'Hyperliquid': ['defi', 'trading'],
    'SynFutures': ['defi', 'derivatives', 'trading'],
    'Rage-Trade': ['defi', 'trading'],
    'Zeta-Markets': ['defi', 'derivatives', 'trading'],
    'IntentX': ['defi', 'trading'],
    'Bluefin': ['defi', 'trading'],
    'Pika': ['defi', 'trading'],
    'Orderly': ['defi', 'order-book', 'cross-chain'],
    'Clipper': ['defi', 'trading', 'liquidity'],
    'Kwenta': ['defi', 'trading', 'perpetuals'],
    'Contango': ['defi', 'trading', 'futures'],

    # DeFi - Yield/Staking
    'Yearn-finance': ['defi', 'yield', 'aggregator'],
    'Pickle-Finance': ['defi', 'yield', 'aggregator'],
    'EigenLayer': ['defi', 'staking', 'restaking'],
    'Eigenpie': ['defi', 'yield'],
    'StakeWise': ['defi', 'staking'],
    'Renzo': ['defi', 'staking', 'liquid-staking'],
    'Lend-Flare': ['defi', 'lending', 'yield'],
    'Convex-Finance': ['defi', 'yield', 'optimizer'],
    'APWine': ['defi', 'yield', 'derivatives'],
    'Element Finance': ['defi', 'yield'],
    'Kamino': ['defi', 'yield', 'optimization'],
    'EtherFi': ['defi', 'staking', 'ethereum'],
    'Aerodrome': ['defi', 'liquidity', 'yield-farming'],
    'Popsicle Finance': ['defi', 'yield', 'multi-strategy'],
    'Gro-Protocol': ['defi', 'yield', 'diversification'],
    'Wombat': ['defi', 'yield', 'optimization'],
    'Swell-Network': ['defi', 'staking', 'ethereum'],
    'Helio-(Lista)': ['defi', 'yield', 'aggregation'],
    'Smoothy-Finance': ['defi', 'yield', 'aggregation'],
    'Elipsis': ['defi', 'yield', 'stablecoin'],
    'Usual': ['defi', 'yield', 'stablecoin'],

    # DeFi - Options
    'Ribbon-Finance': ['defi', 'options'],
    'Thetanuts-Fi': ['defi', 'options'],
    'Lyra': ['defi', 'options'],
    'GammaSwap': ['defi', 'options', 'futures'],
    'Antimatter': ['defi', 'options', 'derivatives'],

    # DeFi - Other
    'Timeless': ['defi', 'time', 'tokenization'],
    'Spin': ['defi', 'interest', 'dynamic-rates'],
    'Equilibre': ['defi', 'balance', 'ecosystem'],
    'Burnt-(XION)': ['defi', 'tokenomics', 'burn-mechanism'],
    'Blast': ['defi', 'growth', 'mechanisms'],
    'Parcl': ['defi', 'real-estate', 'fractional-ownership'],
    'Wen': ['defi', 'time-based', 'smart-contracts'],
    'Ethena': ['defi', 'stablecoins', 'synthetics'],
    'Aevo': ['defi', 'tokenomics', 'economics'],
    'De-Fi': ['defi', 'tools', 'security'],
    'Degen': ['defi', 'high-risk', 'yield-farming'],
    'Quasar': ['defi', 'asset-management', 'cross-chain'],
    'Prisma-Finance': ['defi', 'yield', 'stablecoin'],
    'Islamic-Coin': ['defi', 'sharia-compliant', 'cryptocurrency'],
    'FuruCombo': ['defi', 'strategy', 'automation'],
    'ThorChain': ['defi', 'cross-chain', 'swap'],
    'Mirror-Protocol': ['defi', 'synthetics', 'assets'],
    'Juicebox-DAO': ['defi', 'fundraising', 'dao'],
    'ForeFront': ['defi', 'venture-capital', 'community'],
    'ListaDAO': ['defi', 'dao', 'investment'],
    'Sanctum': ['defi', 'privacy', 'security'],
    'Sharpe': ['defi', 'risk-management', 'analytics'],
    'MON-Protocol': ['defi', 'stablecoin', 'governance'],
    'Penumbra': ['defi', 'privacy', 'zkp'],
    'Tensor': ['defi', 'data', 'analytics'],
    'Fluidity': ['defi', 'liquidity', 'rewards'],
    'Manta': ['defi', 'privacy', 'zkp'],
    'DexGuru': ['defi', 'analytics', 'dex'],
    'IndexCoop': ['defi', 'index', 'tokens'],

    # Gaming/NFT
    'Param-Labs': ['gaming', 'interoperability', 'blockchain'],
    'AlienX': ['gaming', 'defi', 'innovation'],
    'Mocaverse': ['gaming', 'metaverse', 'blockchain'],
    'Notcoin': ['gaming', 'education', 'cryptocurrency'],
    'Magic-Square': ['gaming', 'puzzle', 'blockchain'],
    'Ai-Arena': ['gaming', 'platform'],
    'Nyan-Heroes': ['gaming'],
    'BlockGames': ['gaming', 'platform'],
    'Pentagon-Games': ['gaming', 'platform'],
    'Mavia': ['gaming', 'platform'],
    'GameSwift': ['gaming', 'infrastructure'],
    'zkApe': ['nft', 'gaming', 'zk-rollup'],

    # NFT Marketplaces
    'Blur': ['nft', 'marketplace'],
    'LooksRare': ['nft', 'marketplace'],
    'Magic-Eden': ['nft', 'marketplace'],
    'Exchange-Art': ['nft', 'marketplace'],
    'X2Y2': ['nft', 'marketplace'],
    'Rarible': ['nft', 'marketplace'],
    'ProjectGalaxyHQ': ['nft', 'platform', 'marketplace'],
    'Blur': ['nft', 'seasonal', 'marketplace'],

    # NFT Projects
    'Pudgy-Penguins': ['nft', 'collection'],
    'NFTfi': ['nft', 'defi'],
    'Memeland': ['nft', 'ecosystem'],
    'StarryNift': ['nft', 'platform'],
    'NFPrompt': ['nft', 'platform'],
    'Pixels': ['nft', 'project'],
    'MurALL': ['nft', 'art', 'blockchain'],
    'Botto': ['nft', 'art', 'ai-governance'],

    # Social/Identity
    'CyberConnect': ['social', 'platform'],
    'Phaver': ['social', 'platform'],
    'Galxe': ['social', 'platform', 'quests'],
    'Space-ID': ['identity', 'naming'],
    'Masa-Finance': ['identity', 'protocol'],
    'ENS-Domain': ['identity', 'naming'],
    'Carv.io': ['social', 'platform'],
    'EtherMail': ['social', 'communication'],
    'Dmail': ['social', 'communication'],
    'Developer-DAO': ['social', 'community', 'dao'],
    'Seed-Club': ['social', 'community'],
    'Beoble': ['social', 'platform'],
    'Movement': ['social', 'mobility', 'blockchain'],
    'QnA3': ['social', 'qna', 'blockchain'],
    'SailDAO': ['social', 'governance', 'maritime'],
    'AsMatch': ['social', 'matching', 'blockchain'],

     # Several Infrastructure entries:
    'Mask': ['infrastructure', 'web3'],
    'Shell-Protocol': ['infrastructure', 'defi'],
    'Holograph': ['infrastructure', 'cross-chain'],
    'Polyhedra': ['infrastructure', 'zk'],
    'Forta': ['infrastructure', 'security'],
    'Hats-finance': ['infrastructure', 'dao'],
    'CollabLand': ['infrastructure', 'community'],
    'Omni': ['infrastructure', 'multi-purpose', 'blockchain'],
    'Bonsai': ['infrastructure', 'growth', 'management'],

    # Additional DeFi entries
    'Saddle-Exchange': ['defi', 'stablecoin', 'exchange'],
    'Reflexer-Ungovernance-Token': ['defi', 'stablecoin', 'algorithmic'],
    'Element-Finance': ['defi', 'yield', 'fixed-income'],
    'Ampleforth': ['defi', 'stablecoin', 'rebase'],
    'Pool-Together': ['defi', 'lottery', 'no-loss'],
    'DeFi-Yield-Protocol': ['defi', 'yield', 'protocol'],
    'Lotto-Finance': ['defi', 'gambling', 'lottery'],
    'Thales': ['defi', 'prediction', 'markets'],

    # Additional AI/Data entries
    'Aigisos': ['ai', 'security', 'blockchain'],
    'XAI': ['ai', 'blockchain', 'research'],

    # Misc entries:
    'HAPI': ['health', 'data', 'blockchain'],
    'ionet': ['iot', 'networking', 'blockchain'],
    'Grass': ['environment', 'community', 'blockchain'],
    'Uprock': ['culture', 'art', 'blockchain'],
    'KIP-Protocol': ['identity', 'privacy', 'blockchain'],
    'BounceBit': ['defi', 'token-distribution', 'auctions'],
    'Nostra': ['prediction', 'markets', 'oracles'],
    'Azuro': ['defi', 'betting', 'prediction'],
    'Gitcoin': ['social', 'funding', 'opensource']

  # Social/Community Platforms
    'SNS': ['social', 'platform', 'privacy', 'community'],
    'Hooked': ['social', 'platform', 'rewards', 'content'],
    
    # Infrastructure/Services
    'HashKey Global': ['infrastructure', 'trading', 'custody'],
    'LogX': ['infrastructure', 'data', 'analytics'],
    'Aethir': ['infrastructure', 'computing', 'gpu'],
    
    # Gaming/Metaverse
    'Pirate Nation': ['gaming', 'ecosystem', 'nft'],
    'ZTX': ['gaming', 'metaverse', 'social'],
    
    # DeFi
    'Puffer Finance': ['defi', 'yield', 'optimization'],
    'Badger DAO': ['defi', 'bitcoin', 'dao'],
    
    # NFT/Art
    'Pencil Protocol': ['nft', 'art', 'marketplace']
    }

def update_markdown_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # Extract project name from filename
    filename = os.path.basename(filepath)
    project_name = filename[11:-3]  # Remove date prefix and .md extension

    # Get categories for the project
    categories = category_mapping.get(project_name, ['uncategorized'] )
    categories_str = f"categories: {categories}"

    # Update or add categories in frontmatter
    frontmatter_pattern = r'---\n(.*?\n)---'
    frontmatter_match = re.search(frontmatter_pattern, content, re.DOTALL)

    if frontmatter_match:
        frontmatter = frontmatter_match.group(1)
        new_frontmatter = re.sub(
            r'categories:.*?\n',
            f'{categories_str}\n',
            frontmatter,
            flags=re.MULTILINE
        )
        if 'categories:' not in frontmatter:
            new_frontmatter = f'{new_frontmatter}{categories_str}\n'

        new_content = f'---\n{new_frontmatter}---\n{content[frontmatter_match.end():]}'

        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated categories for {project_name}: {categories}")
    else:
        print(f"No frontmatter found in {filepath}")

def main():
    # Get current directory
    current_dir = os.getcwd()

    # Process all markdown files with the date prefix format
    for filename in os.listdir(current_dir):
        if filename.endswith('.md') and re.match(r'\d{4}-\d{2}-\d{2}-.*\.md', filename):
            filepath = os.path.join(current_dir, filename)
            update_markdown_file(filepath)

if __name__ == "__main__":
    main()
