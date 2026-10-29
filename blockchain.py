@'
const crypto = require("crypto");

class Block {
    constructor(index, data, previousHash = "0") {
        this.index = index;
        this.timestamp = new Date().toISOString();
        this.data = data;
        this.previousHash = previousHash;
        this.hash = this.calculateHash();
    }

    calculateHash() {
        const content = this.index + this.timestamp +
            JSON.stringify(this.data) + this.previousHash;

        return crypto.createHash("sha256")
            .update(content).digest("hex");
    }
}

class Blockchain {
    constructor() {
        this.chain = [new Block(0, "Genesis Block")];
    }

    addBlock(data) {
        const previousBlock = this.chain[this.chain.length - 1];
        const block = new Block(
            this.chain.length, data, previousBlock.hash
        );
        this.chain.push(block);
    }

    isValid() {
        for (let i = 1; i < this.chain.length; i++) {
            const current = this.chain[i];
            const previous = this.chain[i - 1];

            if (current.hash !== current.calculateHash()) return false;
            if (current.previousHash !== previous.hash) return false;
        }
        return true;
    }
}

const myBlockchain = new Blockchain();

myBlockchain.addBlock({
    sender: "Alice",
    receiver: "Bob",
    amount: 100
});

myBlockchain.addBlock({
    sender: "Bob",
    receiver: "Charlie",
    amount: 25
});

console.log("=== SIMPLE BLOCKCHAIN ===");
console.log(JSON.stringify(myBlockchain.chain, null, 2));
console.log("Blockchain valid:", myBlockchain.isValid());
'@ | Set-Content -Encoding utf8 .\blockchain.js