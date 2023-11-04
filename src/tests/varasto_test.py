import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_konstruktori_sallii_negatiivisen_tilavuuden(self):
        # Tarkista, että konstruktori sallii negatiivisen tilavuuden ja asettaa sen nollaksi.
        varasto = Varasto(-5)
        self.assertAlmostEqual(varasto.tilavuus, 0)
    
    def test_konstruktori_alusta_saldon(self):
        # Tarkista, että konstruktori alustaa saldon oikein annetulla alku_saldolla.
        varasto = Varasto(10, 5)
        self.assertAlmostEqual(varasto.saldo, 5)
    
    def test_lisays_negatiivinen_maara_ei_muuta_saldoa(self):
        # Tarkista, ettei negatiivinen lisäys muuta saldoa.
        self.varasto.lisaa_varastoon(5)
        self.varasto.lisaa_varastoon(-2)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_lisays_ylittaa_tilavuuden(self):
        # Tarkista, että lisäys ei ylitä varaston tilavuutta.
        self.varasto.lisaa_varastoon(12)
        self.assertAlmostEqual(self.varasto.saldo, 10)
    
    def test_ottaminen_negatiivinen_maara_ei_muuta_saldoa(self):
        # Tarkista, ettei negatiivinen oton määrä muuta saldoa ja että palautus on nolla.
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(saatu_maara, 0)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_ottaminen_yli_saldon(self):
        # Tarkista, että otto ei voi ylittää saldoa ja palautus on oikea.
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(7)
        self.assertAlmostEqual(saatu_maara, 5)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_konstruktori_negatiivinen_alku_saldo(self):
        # Tarkista, että negatiivinen alku_saldo nollataan.
        varasto = Varasto(10, -5)
        self.assertAlmostEqual(varasto.saldo, 0)
    
    def test_str_metodi_palauttaa_oikean_merkkijonon(self):
        # Tarkista, että __str__ -metodi palauttaa oikean merkkijonon.
        varasto = Varasto(10, 5)
        expected_str = "saldo = 5, vielä tilaa 5"
        self.assertEqual(str(varasto), expected_str)
    

