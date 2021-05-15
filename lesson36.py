# Klasslar bilan ishlash

class A:
    prop1 = "Property 1"
    prop2 = "Property 2"
    name = "Anvar"

    def hi(self, name=""):
        if name:
            return "HI " + name
        else:
            return "HI " + self.name


a = A()

print(a.hi(""))
