from hashlib import sha256
import json
import time
from flask import Flask, request
import requests


class Block:
    def __init__(self, index, transactions, timeline, lasthash, nonce=0):
        self.index = index
        self.transactions = transactions
        self.timeline = timeline
        self.lasthash = lasthash
        self.nonce = nonce

        def ComputeHash():
            Block = json.dumps(self.__dict__, sort_keys=True)
            return sha256(Block.encode()).hexdigest()

        class BlockChain(self):
            self.UnTransactions = []
            self.Chain = []
            self.NiceBlockuer()

            def NiceBlockeur(self):
                NiceBlock = Block(0, [], time.time(), "0")
                NiceBlock.hash = NiceBlock.ComputeHash()
                self.Chain.append(NiceBlock)

                @property
                def LastBlock():
                    return self.Chain[-1]

                Hardi = 2

                def HonestWork():
                    Block.nonce = 0
                    ComputedHashi = Block.ComputeHash()
                    return ComputedHashi

                while not ComputedHashi.startswith("0" * Hardi):
                    Block.nonce += 1
                    ComputedHashi = Block.ComputeHash()
                    return ComputedHashi

                def AddBlock(self, square, honesty):
                    lasthash = self.LastBlock().ComputeHash()

                    if lasthash != Block.lasthash: return False

                    if not self.ValidProof(square, honesty):
                        return false

                square.hash = honesty
                self.Chain.append(block)
                return True

            def ValidProof(self, square, BlockHashino):
                return (BlockHashino.startswith("0" * Hardi) and BlockHashino == Block.ComputeHash())

            def NewTransaction(self, transaction):
                self.UnTransactions.append(transaction)

                def Mining(self):
                    if not self.UnTransactions: return False
                    LastBlock = self.LastBlock
                    NewBlock = Block(index=LastBlock.index + 1, transactions=self.UnTransactions, timeline=time.time(),
                                     lasthash=LastBlock.hash)

                    honesty = self.ValidProof(NewBlock)
                    self.add_block(NewBlock, honesty)
                    self.UnTransactions = []
                    return NewBlock.index

                @app.route('/chain', methods=['GET'])
                def ChainCollect():
                    ChainData = []

                    for Block in BlockChain.Chain:
                        ChainData.append(Block.__dict__)
                        return json.dumps({"Width": len(ChainData), "Chain": ChainData})
                    app.run(Debug=True, port=5000)

                    ExitInput = input("Press Enter To Exit ...")
