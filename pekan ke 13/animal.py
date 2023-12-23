class Animal:
    def __init__(self, name, food, habitat, reproduction):
        self.name = name
        self.food = food
        self.habitat = habitat
        self.reproduction = reproduction

class Rhino(Animal):
    def __init__(self, name, habitat):
        super().__init__(name, "tumbuhan", habitat, "vivipar")

    def keterangan(self):
        return "pemalu dan sensitif"

class Fish(Animal):
    def __init__(self, name, habitat):
        super().__init__(name, "plankton", habitat, "ovipar")

    def swim(self):
        return "Berenang dengan anggun di air."

class Snake(Animal):
    def __init__(self, name, habitat):
        super().__init__(name, "tikus", habitat, "ovovivipar")

    def keterangan(self):
        return "agresif dan racun yang kuat."
    

class Horse(Animal):
    def __init__(self, name, habitat):
        super().__init__(name, "rumput", habitat, "vivipar")

    def keterangan(self):
        return "berlari cepat dengan anggun."
    
class Lion(Animal):
    def __init__(self, name, habitat):
        super().__init__(name, "rusa", habitat, "vivipar")

    def keterangan(self):
        return "raja hutan."
    

badak = Rhino("Badak Jawa", "Hutan")
print(f"{badak.name} hidup di {badak.habitat}, makan {badak.food}, dan berkembang biak secara {badak.reproduction}.")
print(f"{badak.name} memiliki sifat: {badak.keterangan()}")

ikan = Fish("Ikan Koi", "Air Tawar")
print(f"{ikan.name} hidup di {ikan.habitat}, makan {ikan.food}, dan berkembang biak secara {ikan.reproduction}.")
print(f"{ikan.name} bisa: {ikan.swim()}")

ular = Snake("Ular Cobra", "Hutan")
print(f"{ular.name} hidup di {ular.habitat}, makan {ular.food}, dan berkembang biak secara {ular.reproduction}.")
print(f"{ular.name} memiliki sifat: {ular.keterangan()}")

kuda = Horse("Kuda Friesian ", "sabana")
print(f"{kuda.name} hidup di {kuda.habitat}, makan {kuda.food}, dan berkembang biak secara {kuda.reproduction}.")
print(f"{kuda.name} bisa: {kuda.keterangan()}")

singa = Lion("Singa Afrika", "sabana")
print(f"{singa.name} hidup di {singa.habitat}, makan {singa.food}, dan berkembang biak secara {singa.reproduction}.")
print(f"{singa.name} adalah: {singa.keterangan()}")