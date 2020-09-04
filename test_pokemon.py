# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 14:02:57 2020

@author: Mei
"""

import unittest
from pokemon import Pokemon


class PokemonTests(unittest.TestCase):
    def setUp(self):
        self.pokemon = Pokemon('pokedex.csv')

    def test_get_boss_url_existing(self):
        self.assertGreater(len(self.pokemon.get_boss_url('Heatran')), 0)
        self.assertGreater(len(self.pokemon.get_boss_url('golem')), 0)
        self.assertGreater(len(self.pokemon.get_boss_url('alolan raichu')), 0)

    def test_get_boss_url_fuzzy(self):
        self.assertGreater(len(self.pokemon.get_boss_url('wheezing')), 0)

    def test_get_boss_url_nonexisting(self):
        self.assertEqual(len(self.pokemon.get_boss_url('afsdf')), 0)

    def test_get_boss_url_case_insensitive(self):
        self.assertGreater(len(self.pokemon.get_boss_url('pikachu')), 0)
        self.assertEqual(self.pokemon.get_boss_url('PikAchu'),
                         self.pokemon.get_boss_url('pikachu'))

    def test_find_found(self):
        self.assertEqual(self.pokemon.find('venusaur'), 'venusaur')
        self.assertEqual(self.pokemon.find('Venusaur'), 'venusaur')

        self.assertEqual(self.pokemon.find('venasaur'), 'venusaur')
        self.assertEqual(self.pokemon.find('venusar'), 'venusaur')
        self.assertEqual(self.pokemon.find('veenusaur'), 'venusaur')

        self.assertEqual(self.pokemon.find('mega charizard x'),
                         'mega charizard x')
        self.assertEqual(self.pokemon.find('maga charizard x'),
                         'mega charizard x')

    def test_find_not_found(self):
        self.assertEqual(self.pokemon.find('mega charizard'),
                         '')


if __name__ == '__main__':
    unittest.main()
