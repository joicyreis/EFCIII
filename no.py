class No:
    def __init__(self, ind):
        self.num = ind
        self.cores_bloqueadas = []
        self.conexoes = []
        self.cor = None

    # define uma cor para o nó em questão
    # se não conseguir utilizar retorna None
    def define_cor(self, cores):
        for c in cores:
            if c not in self.cores_bloqueadas:
                self.cor = c
                self.bloqueia_cor()
                return 0
        return None

    # bloqueia a cor do nó em seus vizinhos
    def bloqueia_cor(self):
        for n in self.conexoes:
            n.cores_bloqueadas.append(self.cor)
