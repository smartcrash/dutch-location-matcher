from location_matcher import LocationMatcher

location_matcher = LocationMatcher()


def test_1(self):
    text = """Al ruim twee jaar rookt bij elke frisse dag de houtkachel aan de Fluitekamp in Hoogland."""

    span = location_matcher(text)

    self.assertIsNotNone(span)
    self.assertEqual(span.text, 'Fluitekamp in Hoogland')


def test_2(self):
    text = """Terwijl dit gesprek door gaat, komt een man de Hema in Montfoort binnen en rekent twee powerbanks af met de pas van het slachtoffer."""
    span = location_matcher(text)

    self.assertIsNotNone(span)
    self.assertEqual(span.text, 'Hema in Montfoort')


def test_3(self):
    text = """Was u getuige van de aanval in de Maarssense wijk Zwanenkamp op woensdag 1 februari? Bel dan met de tiplijn: 0800 - 6070 of bel Meld Misdaad Anoniem: 0800 - 7000. Beelden waarop de dader te zien is kunt u uploaden via politie.nl/upload"""
    span = location_matcher(text)

    self.assertIsNotNone(span)
    self.assertEqual(span.text, 'Maarssense wijk Zwanenkamp')


def test_4(self):
    text = """Er is veel chemie op de werkvloer, de cultuur is hier heel goed.""  VERJAARDAG MET DE KONING EN MINISTER YESILGÖZ  Het 75-jarige jubileum van de vrijwillige politie werd vandaag gevierd bij evenementenlocatie Mereveld in Utrecht."""
    span = location_matcher(text)

    self.assertIsNotNone(span)
    self.assertEqual(span.text, 'Mereveld in Utrecht')


def test_5(self):
    text = """Vleuten - Zondagavond 12 maart rond 22.30 uur was er een explosie bij een woning aan de Moersbergen in Vleuten."""
    span = location_matcher(text)

    self.assertIsNotNone(span)
    self.assertEqual(span.text, 'Moersbergen in Vleuten')


def test_6(self):
    text = """Utrecht - Straatafval, drugshandel, geluidoverlast en intimidatie. Bewoners van een flat aan de Marco Pololaan in de Utrechtse wijk Kanaleneiland zijn naar eigen zeggen al jaren met politie en gemeente in de weer om de overlast van een groep hangjongeren en volwassen mannen in hun straat te weren, vooralsnog zonder resultaat."""
    span = location_matcher(text)

    self.assertIsNotNone(span)
    self.assertEqual(
        span.text, 'Marco Pololaan in de Utrechtse wijk Kanaleneiland')


def test_7(self):
    text = """Vleuten - Zondagavond 12 maart rond 22.30 uur was er een explosie bij een woning aan de Moersbergen in Vleuten."""
    span = location_matcher(text)

    self.assertIsNotNone(span)
    self.assertEqual(span.text, 'Moersbergen in Vleuten')


def test_8(self):
    text = """Zeist - Op 7 februari steelt een man voor zo'n 300 euro aan tandpasta en andere mondverzorgingsproducten bij de Kruidvat in Zeist."""
    span = location_matcher(text)

    self.assertIsNotNone(span)
    self.assertEqual(span.text, 'Kruidvat in Zeist')


def test_9(self):
    text = """Het gaat om een gebouw aan de Parklaan in de wijk Molenvliet en om een woningbouwgebied dat nog ontwikkeld moet worden bij Snellerpoort en het Stationsgebied."""
    span = location_matcher(text)

    self.assertIsNotNone(span)
    self.assertEqual(span.text, 'Parklaan in de wijk Molenvliet')


def test_10(self):
    text = """Benschop - In één maand tijd is bij drie muziekstudio's ingebroken. Bij de eerste inbraak bij 'Barn in de Meadow' in Benschop verdwenen onder andere gitaren van de Utrechtse band Kensington."""
    span = location_matcher(text)

    self.assertIsNotNone(span)
    self.assertEqual(span.text, 'Benschop')


def test_11(self):
    text = """Wilnis - Een 84-jarige vrouw en haar 59-jarige zoon zijn in de nacht van 5 op 6 maart met geweld overvallen in hun woning in Wilnis."""
    span = location_matcher(text)

    self.assertIsNotNone(span)
    self.assertEqual(span.text, 'Wilnis')


def test_12(self):
    text = """De proef met het inzamelen van lege flesjes op station Utrecht Centraal wordt uitgebreid: vanaf 1 april kun je ook blikjes inleveren voor statiegeld."""
    span = location_matcher(text)

    self.assertIsNotNone(span)
    self.assertEqual(span.text, 'station Utrecht Centraal')


def test_13(self):
    text = """Anouar T., een neef van vermeend topcrimineel Ridouan T., heeft maandag tijdens zijn voorgeleiding de rechter-commissaris van de rechtbank in Zwolle gewraakt. Hij werd vrijdag opgepakt in Utrecht."""
    span = location_matcher(text)

    self.assertIsNotNone(span)
    self.assertEqual(span.text, 'Utrecht')


def test_14(self):
    text = """In Utrecht hoeven jongeren met een bijstandsuitkering niet eerst vier weken te wachten voor ze geld krijgen."""
    span = location_matcher(text)

    self.assertIsNotNone(span)
    self.assertEqual(span.text, 'Utrecht')


def test_15(self):
    text = """Bilthoven - De advocaat van Utrechtse crimineel Ridouan T."""
    span = location_matcher(text)

    self.assertIsNotNone(span)
    self.assertEqual(span.text, 'Bilthoven')


def test_17(self):
    text = """Op de A2 bij Utrecht is een vrachtwagen op een pilaar gebotst. De chauffeur zat bekneld in de cabine maar is door de brandweer bevrijdt."""
    span = location_matcher(text)

    self.assertIsNotNone(span)
    self.assertEqual(span.text, 'A2 bij Utrecht')


def test_18(self):
    text = """Burgemeester Gilbert Isabella van Houten heeft een dwangsom van maximaal 6000 euro opgelegd na de ontdekking van drugshandel en illegale bewoning."""
    span = location_matcher(text)

    self.assertIsNotNone(span)
    self.assertEqual(span.text, 'Houten')


def test_19(self):
    text = """Provincie Utrecht - De huizenprijzen zijn in het eerste kwartaal van dit jaar het hardst gedaald in de provincie Utrecht, namelijk met 3 procent ten opzichte van de eerste drie maanden van vorig jaar."""
    span = location_matcher(text)

    self.assertIsNotNone(span)
    self.assertEqual(span.text, 'Provincie Utrecht')


def test_20(self):
    text = """Provincie Utrecht - Trapper niet in!, is de campagne die de provincie heeft gelanceerd om Utrechters bewuster te maken van de risico's van dronken op de fiets stappen. Want beschonken fietsers belanden steeds vaker en met hevigere verwondingen op de eerste hulp, valt ook de ziekenhuizen op."""
    span = location_matcher(text)

    self.assertIsNotNone(span)
    self.assertEqual(span.text, 'Provincie Utrecht')


def test_21(self):
    text = """Toen was er inderdaad sprake van een lek, Kasteel Heemstede werd op die manier overrompeld met een ster."""
    span = location_matcher(text)

    self.assertIsNotNone(span)
    self.assertEqual(span.text, 'Kasteel Heemstede')


def test_22(self):
    text = """De agenten hielden rond 5.00 uur 's nachts toezicht op uitgaanspubliek op de Hof, waar ze twee mannen aanspraken op hun gedrag."""
    span = location_matcher(text)

    self.assertIsNotNone(span)
    self.assertEqual(span.text, 'de Hof')


def test_23(self):
    text = """Het ging afgelopen vrijdag mis op de Biltse Rading toen de vrouw met twee kinderen overstak op een oversteekplaats tussen de Voorveldse Polder en de Veemarkt."""
    span = location_matcher(text)

    self.assertIsNotNone(span)
    self.assertEqual(
        span.text, 'oversteekplaats tussen de Voorveldse Polder en de Veemarkt')


def test_24(self):
    text = """De eerste wedstrijd om het landskampioenschap werd vandaag precies 125 jaar geleden gespeeld op het veld van USV Hercules in Utrecht."""
    span = location_matcher(text)

    self.assertIsNotNone(span)
    self.assertEqual(span.text, 'USV Hercules in Utrecht')


def test_25(self):
    text = """In de Utrechtse binnenstad nam de chauffeur van lijn 74 een verkeerde afslag en belandde op de Nieuwegracht, waar de harmonicabus geen kant meer op kon."""
    span = location_matcher(text)

    self.assertIsNotNone(span)
    self.assertEqual(span.text, 'Nieuwegracht')


def test_26(self):
    text = """In het buitengebied van Groenekan vlakbij Voordaan komt een zonneveld van ongeveer 17 hectare."""
    span = location_matcher(text)

    self.assertIsNotNone(span)
    self.assertEqual(span.text, 'Groenekan vlakbij Voordaan')


def test_27(self):
    text = """In Nederland zwaaien de klokken heen en weer en dat is in feite bim bam." Wanneer je bovenin de Onze Lieve Vrouwetoren in Amersfoort staat om naar de enorme klokken te kijken, dan moet je goede gehoorbescherming dragen wanneer ze geluid worden."""
    span = location_matcher(text)

    self.assertIsNotNone(span)
    self.assertEqual(span.text, 'Lieve Vrouwetoren in Amersfoort')


def test_28(self):
    text = """Na het overlijden van de laatste brugwachter Stok in mei 1945, kwam het brugwachtershuisje naast de Evert Stokbrug in Maarssen leeg te staan."""
    span = location_matcher(text)

    self.assertIsNotNone(span)
    self.assertEqual(span.text, 'Evert Stokbrug in Maarssen')


def test_29(self):
    text = """Op de A1 bij de afslag Baarn - Soest is een auto met caravan gecrasht."""
    span = location_matcher(text)

    self.assertIsNotNone(span)
    self.assertEqual(span.text, 'A1 bij de afslag Baarn')


def test_30(self):
    text = """Bij Collectief Eemland zijn ze daar blij mee, want de weidevogel zit in groten getale in de Eempolder."""
    span = location_matcher(text)

    self.assertIsNotNone(span)
    self.assertEqual(span.text, 'in de Eempolder')


def test_31(self):
    text = """Het Comité Joods Monument Baarn is na onderzoek meer te weten gekomen over de identiteit van achttien leerlingen die op de klassenfoto staan."""
    span = location_matcher(text)

    self.assertIsNotNone(span)
    self.assertEqual(span.text, 'Baarn')


def test_32(self):
    text = """Bij het hoofdkantoor bij de Rabobank in Utrecht zijn vanochtend leden van Extinction Rebellion en Christian Climate Action op het dak geklommen om een spandoek op te hangen."""
    span = location_matcher(text)

    self.assertIsNotNone(span)
    self.assertEqual(span.text, 'Rabobank in Utrecht')
