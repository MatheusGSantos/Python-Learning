#source: https://leimao.github.io/blog/Byte-Pair-Encoding/
from collections import defaultdict
import re


class BPE:
    def __init__(self):
        self.vocab = defaultdict(int)

    def get_vocab(self, filename):
        """Get vocabulary dictionary count for each word in the file.
        
        Arguments:
            filename {string} -- name of the file to be read.
        """
        try:
            f = open(filename, 'r', encoding='utf-8')
        except FileNotFoundError as e:
            print(e)
        else:
            lines = (line for line in f)
            for line in lines:
                words = line.strip().split()
                for word in words:
                    self.vocab[' '.join(list(word))+'</w>'] +=1
            f.close()


    def get_stats(self):
        """Get the frequency of each pair of symbols in each word of vocab.
        
        Returns:
            defaultdict(int) -- dictionary of pair frequencies
        """
        pairs = defaultdict(int)
        for word, freq in self.vocab.items():
            symbols = word.split()
            for i in range(len(symbols)-1):
                pairs[symbols[i],symbols[i+1]] += freq
        return pairs
            

    def merge_vocab(self, pair):
        """Merges pair of tokens.
        
        Arguments:
            pair {tuple(str, str)} -- most recurrent pair of tokens
        
        Returns:
            dict -- returns the token-merged version of vocab
        """
        v_out = dict()
        bigram = re.escape(' '.join(pair))
        p = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
        for word in self.vocab:
            w_out = p.sub(''.join(pair), word)
            v_out[w_out] = self.vocab[word]
        return v_out        


    def run(self, filename, n_merges):
        """Runs BPE algorithm.
        
        Arguments:
            filename {string} -- name of the file to be read.
            n_merges {int} -- maximum number of merges.
        """
        self.get_vocab(filename)
        i = 0
        while i < n_merges:
            print("Running iteration #"+str(i),end='\r')
            pairs = self.get_stats()

            if not pairs:
                break
            best = max(pairs, key=pairs.get)
            self.vocab = self.merge_vocab(best)
            i += 1
        print("\nDone")


    def clear_vocab(self):
        """Resets Vocab.
        """
        self.vocab = defaultdict(int)


    def to_JSON(self, filename):
        """Exports vocab dict to JSON file.
        
        Arguments:
            filename {string} -- name of json file (must include .json extension)
        """
        import json
        with open(filename, 'w', encoding="utf-8") as output:   # write to Json file
            json.dump(self.vocab, output, ensure_ascii=False, indent=4)

    
"""
if __name__ == '__main__':
    bpe = BPE()
    bpe.run('pg16457.txt', 100)
    bpe.to_JSON('test.json')
"""
