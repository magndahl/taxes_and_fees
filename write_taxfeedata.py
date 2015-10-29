# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 13:53:14 2015

@author: Magnus Dahl
"""
from taxfee_classes import Taxfee

# Write and save Danish taxes and fees on electricity for heat pumps and
# electric boilers for 2014- oct 2015

PSO = Taxfee('PSO')
PSO.add_row_quick(190, 2014, 1, 1, 2014, 3, 31)
PSO.add_row_quick(227, 2014, 4, 1, 2014, 6, 30)
PSO.add_row_quick(217, 2014, 7, 1, 2014, 9, 30)
PSO.add_row_quick(230, 2014, 10, 1, 2014, 12, 31)
PSO.add_row_quick(211, 2015, 1, 1, 2015, 3, 31)
PSO.add_row_quick(214, 2015, 4, 1, 2015, 6, 30)
PSO.add_row_quick(218, 2015, 7, 1, 2015, 9, 30)
PSO.save_data('PSO.pkl', 'Taxfee_data/')

EltransNRGI = Taxfee('Eltransport NRGI')
EltransNRGI.add_row_quick(38.9, 2014, 1, 1, 2014, 6, 30)
EltransNRGI.add_row_quick(39.2, 2014, 7, 1, 2014, 12, 31)
EltransNRGI.add_row_quick(42, 2015, 1, 1, 2015, 6, 30)
EltransNRGI.add_row_quick(49, 2015, 7, 1, 2015, 9, 30)
EltransNRGI.save_data('EltransNRGI.pkl', 'Taxfee_data/')

ElsparNRGI = Taxfee('Elsparetarif NRGI')
ElsparNRGI.add_row_quick(16.1, 2014, 1, 1, 2014, 12, 31)
ElsparNRGI.add_row_quick(21.4, 2015, 1, 1, 2015, 9, 30)
ElsparNRGI.save_data('ElsparNRGI.pkl', 'Taxfee_data/')

EltransEnerginetdk = Taxfee('Eltransport Energinet.dk')
EltransEnerginetdk.add_row_quick(69, 2014, 1, 1, 2014, 12, 31)
EltransEnerginetdk.add_row_quick(71, 2015, 1, 1, 2015, 9, 30)
EltransEnerginetdk.save_data('EltransEnerginetdk.pkl', 'Taxfee_data/')

Elafgift = Taxfee('Elafgift varmepumper')
Elafgift.add_row_quick(412, 2014, 1, 1, 2014, 12, 31)
Elafgift.add_row_quick(380, 2015, 1, 1, 2015, 12, 31)
Elafgift.save_data('Elafgift.pkl', 'Taxfee_data/')

Elpatronsats = Taxfee('Afgift på varme efter elpatronordningen')
Elpatronsats.add_row_quick(263, 2014, 1, 1, 2014, 12, 31)
Elpatronsats.add_row_quick(212, 2015, 1, 1, 2015, 12, 31)
Elpatronsats.save_data('Elpatronsats.pkl', 'Taxfee_data/')