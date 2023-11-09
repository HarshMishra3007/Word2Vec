# word_embedder.py
class WordEmbedder:
    def __init__(self, word2vec_model):
        self.word2vec_model = word2vec_model

    def get_embedding(self, word):
        return self.word2vec_model[word] if word in self.word2vec_model else None