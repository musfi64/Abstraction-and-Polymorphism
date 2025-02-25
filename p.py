class usa():
    def capital(self):
        print("washington dc is the capital of usa")
    def language(self):
       print("english is the primary language")
class uk():
    def capital(self):
        print("london is the capital of uk")
    def language(self):
        print("british english is the primary language")
ob_usa=usa()
ob_uk=uk()
for country in(ob_usa, ob_uk):
    country.capital()
    country.language()