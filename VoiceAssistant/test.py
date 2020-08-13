import re

mystring = "Azerbaijan (UK:  (listen), US: ; Azerbaijani: Azərbaycan [ɑːzæɾbɑjˈd͡ʒɑn]), officially the Republic of Azerbaijan (Azerbaijani: Azərbaycan Respublikası [ɑːzæɾbɑjˈd͡ʒɑn ɾespublikɑˈsɯ]), is a country in the Caucasus region of Eurasia. Located at the crossroads of Eastern Europe and Western Asia, it is bounded by the Caspian Sea to the east, Russia to the north, Georgia to the northwest, Armenia to the west and Iran to the south. The exclave of Nakhchivan is bounded by Armenia to the north and east, Iran to the south and west, and has an 10 km (6.2 mi) long border with Turkey in the northwest."

test = re.sub("[\[].*?[\]]", "", mystring)
print(test)