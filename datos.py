class Datos(object):
    @classmethod
    def medido(self):
        x = []
        medido = []
        with open('Potencial de acción medido.txt') as f:
            for l in f:
                t = l.partition(';')
                x.append(int(t[0]))
                medido.append(self.parsefloat(t[2])) 
            f.close()
        return [x,medido]
    @classmethod
    def modeloDerivadas(self):
        x = []
        modelo = []
        with open('Potencial de acción modelo derivadas.txt') as f:
            for l in f:
                t = l.partition(';')
                x.append(self.parsefloat(t[0]))
                modelo.append(self.parsefloat(t[2]))
            f.close()
        return [x,modelo]
    @classmethod
    def modelo(self):
        x = []
        modelo = []
        with open('Potencial de acción modelo.txt') as f:
            for l in f:
                t = l.partition(';')
                x.append(self.parsefloat(t[0]))
                modelo.append(self.parsefloat(t[2]))
            f.close()
        return [x,modelo]
    @classmethod
    def parsefloat(self,s):
        return float(s.strip().replace(',','.'))
