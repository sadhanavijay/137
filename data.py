# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 13:52:45 2020

@author: Vishal
"""

data = [{'name': 'Sun', 'mass': 1.0, 'radius': 1.0, 'distance': 1.5813e-05, 'gravity': 274.2691614595739}, {'name': 'Sirius', 'mass': 2.1, 'radius': 1.71, 'distance': 8.6, 'gravity': 196.97179955032502}, {'name': 'Canopus', 'mass': 15.0, 'radius': 71.0, 'distance': 310.0, 'gravity': 0.8161153386021839}, {'name': 'Alpha Centauri', 'mass': 1.1, 'radius': 1.2, 'distance': 4.4, 'gravity': 209.51116500384126}, {'name': 'Arcturus', 'mass': 1.1, 'radius': 26.0, 'distance': 37.0, 'gravity': 0.4462959727892475}, {'name': 'Vega', 'mass': 2.2, 'radius': 2.7, 'distance': 25.0, 'gravity': 82.76984296448046}, {'name': 'Capella', 'mass': 2.6, 'radius': 12.0, 'distance': 43.0, 'gravity': 4.952082081908975}, {'name': 'Rigel', 'mass': 23.0, 'radius': 78.9, 'distance': 860.0, 'gravity': 1.0133297854321701}, {'name': 'Procyon', 'mass': 1.5, 'radius': 1.9, 'distance': 11.4, 'gravity': 113.96225545411659}, {'name': 'Betelgeuse', 'mass': 20.0, 'radius': 950.0, 'distance': 640.0, 'gravity': 0.006077986957552886}, {'name': 'Achernar', 'mass': 6.7, 'radius': 9.3, 'distance': 144.0, 'gravity': 21.246425965766498}, {'name': 'Hadar', 'mass': 10.5, 'radius': 8.6, 'distance': 390.0, 'gravity': 38.93761756794925}, {'name': 'Altair', 'mass': 1.8, 'radius': 1.8, 'distance': 17.0, 'gravity': 152.37175636642996}, {'name': 'Acrux', 'mass': 18.0, 'radius': 8.9, 'distance': 320.0, 'gravity': 62.32603088337749}, {'name': 'Aldebaran', 'mass': 1.5, 'radius': 44.0, 'distance': 65.0, 'gravity': 0.21250193294905007}, {'name': 'Antares', 'mass': 12.0, 'radius': 680.0, 'distance': 600.0, 'gravity': 0.0071177118025841}, {'name': 'Spica', 'mass': 11.43, 'radius': 7.47, 'distance': 260.0, 'gravity': 56.18003500809}, {'name': 'Pollux', 'mass': 1.9, 'radius': 8.8, 'distance': 34.0, 'gravity': 6.729227876719916}, {'name': 'Fomalhaut', 'mass': 1.9, 'radius': 1.8, 'distance': 25.0, 'gravity': 160.83685394234269}, {'name': 'Deneb', 'mass': 19.0, 'radius': 203.0, 'distance': 2600.0, 'gravity': 0.12645572733460908}, {'name': 'Mimosa', 'mass': 16.0, 'radius': 8.4, 'distance': 350.0, 'gravity': 62.192553618951}, {'name': 'Regulus', 'mass': 3.8, 'radius': 3.1, 'distance': 77.0, 'gravity': 108.45190567600218}, {'name': 'Adhara', 'mass': 12.5, 'radius': 14.0, 'distance': 430.0, 'gravity': 17.491655705329972}, {'name': 'Shaula', 'mass': 14.5, 'radius': 8.8, 'distance': 700.0, 'gravity': 51.35463379602042}, {'name': 'Castor', 'mass': 2.8, 'radius': 2.4, 'distance': 52.0, 'gravity': 133.3252868206262}, {'name': 'Gacrux', 'mass': 1.5, 'radius': 84.0, 'distance': 88.0, 'gravity': 0.05830551901776656}, {'name': 'Bellatrix', 'mass': 8.6, 'radius': 5.8, 'distance': 240.0, 'gravity': 70.11637302474244}, {'name': 'Elnath', 'mass': 5.0, 'radius': 4.2, 'distance': 130.0, 'gravity': 77.74069202368877}, {'name': 'Miaplacidus', 'mass': 3.5, 'radius': 6.8, 'distance': 110.0, 'gravity': 20.759992757536963}, {'name': 'Alnilam', 'mass': 32.0, 'radius': 42.0, 'distance': 2000.0, 'gravity': 4.9754042895160815}, {'name': 'Gamma Velorum', 'mass': 9.0, 'radius': 6.0, 'distance': 1100.0, 'gravity': 68.56729036489348}, {'name': 'Alnair', 'mass': 4.0, 'radius': 3.4, 'distance': 101.0, 'gravity': 94.90282403445462}, {'name': 'Alioth', 'mass': 2.9, 'radius': 4.2, 'distance': 81.0, 'gravity': 45.089601373739484}, {'name': 'Alnitak', 'mass': 33.0, 'radius': 20.0, 'distance': 1050.0, 'gravity': 22.627205820414854}, {'name': 'Dubhe', 'mass': 4.25, 'radius': 30.0, 'distance': 120.0, 'gravity': 1.2951599291146547}, {'name': 'Mirfak', 'mass': 8.5, 'radius': 68.0, 'distance': 590.0, 'gravity': 0.5041712526830403}, {'name': 'Wezen', 'mass': 17.0, 'radius': 200.0, 'distance': 1600.0, 'gravity': 0.11656439362031895}, {'name': 'Sargas', 'mass': 5.7, 'radius': 26.0, 'distance': 270.0, 'gravity': 2.3126245862715558}, {'name': 'Kaus Australis', 'mass': 3.5, 'radius': 6.8, 'distance': 140.0, 'gravity': 20.759992757536963}, {'name': 'Avior', 'mass': 9.0, 'radius': 130.0, 'distance': 630.0, 'gravity': 0.14606050018557193}, {'name': 'Alkaid', 'mass': 6.1, 'radius': 3.4, 'distance': 104.0, 'gravity': 144.7268066525433}, {'name': 'Menkalinan', 'mass': 2.39, 'radius': 2.77, 'distance': 81.0, 'gravity': 85.43097080483021}, {'name': 'Atria', 'mass': 7.0, 'radius': 92.0, 'distance': 390.0, 'gravity': 0.22682941046987445}, {'name': 'Alhena', 'mass': 2.8, 'radius': 3.3, 'distance': 109.0, 'gravity': 70.51915997124031}, {'name': 'Peacock', 'mass': 5.9, 'radius': 4.8, 'distance': 180.0, 'gravity': 70.23385645015132}, {'name': 'Alsephina[2]', 'mass': 2.4, 'radius': 2.9, 'distance': 80.0, 'gravity': 78.26943965552645}, {'name': 'Mirzam', 'mass': 13.5, 'radius': 10.0, 'distance': 500.0, 'gravity': 37.0263367970425}, {'name': 'Polaris', 'mass': 5.4, 'radius': 39.0, 'distance': 430.0, 'gravity': 0.973736667903813}, {'name': 'Alphard', 'mass': 3.0, 'radius': 50.0, 'distance': 180.0, 'gravity': 0.32912299375148873}, {'name': 'Scheat', 'mass': 2.1, 'radius': 95.0, 'distance': 196.0, 'gravity': 0.0638188630543053}, {'name': 'Almaaz', 'mass': 15.0, 'radius': 140.0, 'distance': 653.0, 'gravity': 0.20989986846395964}, {'name': 'Rasalgethi', 'mass': 2.8, 'radius': 280.0, 'distance': 360.0, 'gravity': 0.00979532719498478}, {'name': 'Tau Ceti', 'mass': 0.7829999999999999, 'radius': 0.893, 'distance': 11.9, 'gravity': 269.2996711047934}, {'name': 'Delta Pavonis', 'mass': 0.991, 'radius': 1.22, 'distance': 19.92, 'gravity': 182.61269753187165}, {'name': 'Ran', 'mass': 0.82, 'radius': 0.74, 'distance': 10.48, 'gravity': 410.7025427261697}, {'name': 'V382 Carinae', 'mass': 20.0, 'radius': 485.0, 'distance': 8900.0, 'gravity': 0.023319728894426524}, {'name': 'Eta Carinae', 'mass': 100.0, 'radius': 881.0, 'distance': 7500.0, 'gravity': 0.035336632665075154}, {'name': 'Delta Cephei', 'mass': 4.5, 'radius': 44.5, 'distance': 887.0, 'gravity': 0.6232603088337749}, {'name': 'Mu Cephei', 'mass': 19.2, 'radius': 972.0, 'distance': 6000.0, 'gravity': 0.005573726798954914}, {'name': 'Titawin', 'mass': 1.27, 'radius': 1.48, 'distance': 44.25, 'gravity': 159.02202111653529}, {'name': 'Rho Cassiopeiae', 'mass': 22.0, 'radius': 800.0, 'distance': 8154.0, 'gravity': 0.009428002425172857}, {'name': 'P Cygni', 'mass': 30.0, 'radius': 76.0, 'distance': 5545.0, 'gravity': 1.4245281931764575}, {'name': 'VV Cephei', 'mass': 18.2, 'radius': 750.0, 'distance': 4900.0, 'gravity': 0.008874131090780881}, {'name': '61 Cygni', 'mass': 0.7, 'radius': 0.665, 'distance': 11.41, 'gravity': 434.14192553949164}, {'name': 'R Doradus', 'mass': 0.8, 'radius': 298.0, 'distance': 178.0, 'gravity': 0.00247078204999391}, {'name': 'Polaris Australis', 'mass': 1.59, 'radius': 3.74, 'distance': 281.0, 'gravity': 31.17675417660804}, {'name': 'R Coronae Borealis', 'mass': 0.85, 'radius': 85.0, 'distance': 4566.0, 'gravity': 0.032266960171714584}, {'name': '54 Piscium', 'mass': 0.76, 'radius': 0.94, 'distance': 36.1, 'gravity': 235.9037604224493}, {'name': 'Mira', 'mass': 1.2, 'radius': 370.0, 'distance': 300.0, 'gravity': 0.00240411244522636}, {'name': 'RW Cephei', 'mass': 13.9, 'radius': 1158.0, 'distance': 14000.0, 'gravity': 0.0028429856016179986}, {'name': 'Lacaille 8760', 'mass': 0.6, 'radius': 0.51, 'distance': 12.87, 'gravity': 632.6854935630311}, {'name': 'V838 Monocerotis', 'mass': 0.5, 'radius': 450.0, 'distance': 19896.0, 'gravity': 0.0006772078060730221}, {'name': 'HD 140283', 'mass': 2.0, 'radius': 1.4, 'distance': 190.0, 'gravity': 279.86649128527955}, {'name': 'II Pegasi', 'mass': 0.8, 'radius': 3.4, 'distance': 130.0, 'gravity': 18.98056480689093}, {'name': 'VY Canis Majoris', 'mass': 17.0, 'radius': 1420.0, 'distance': 3900.0, 'gravity': 0.0023123267927061875}, {'name': 'Pistol Star', 'mass': 100.0, 'radius': 320.0, 'distance': 25000.0, 'gravity': 0.2678409779878652}, {'name': 'S Doradus', 'mass': 24.0, 'radius': 380.0, 'distance': 169000.0, 'gravity': 0.04558490218164664}, {'name': 'UY Scuti', 'mass': 7.0, 'radius': 755.0, 'distance': 5100.0, 'gravity': 0.0033680700499399453}, {'name': "Barnard's Star", 'mass': 0.14, 'radius': 0.2, 'distance': 5.98, 'gravity': 959.9420651085088}, {'name': 'Luhman 16', 'mass': 0.04, 'radius': 0.02, 'distance': 6.52, 'gravity': 27426.916145957402}, {'name': 'Proxima Centauri', 'mass': 0.12, 'radius': 0.15, 'distance': 4.25, 'gravity': 1462.7688611177273}, {'name': 'KIC 8462852', 'mass': 1.43, 'radius': 1.58, 'distance': 1470.0, 'gravity': 157.10819615734286}, {'name': 'R136a1', 'mass': 290.0, 'radius': 32.0, 'distance': 163000.0, 'gravity': 77.67388361648091}, {'name': 'Melnick 42', 'mass': 189.0, 'radius': 21.1, 'distance': 163000.0, 'gravity': 116.43240609119171}, {'name': 'WR 102', 'mass': 19.0, 'radius': 0.39, 'distance': 18134.0, 'gravity': 34261.104981800825}, {'name': 'VFTS 352', 'mass': 57.48, 'radius': 14.47, 'distance': 164000.0, 'gravity': 75.29335961731134}, {'name': 'YBP 1194', 'mass': 1.01, 'radius': 0.99, 'distance': 2772.0, 'gravity': 282.6363157577489}, {'name': 'Gliese 1214', 'mass': 0.16, 'radius': 0.21, 'distance': 47.5, 'gravity': 995.0808579032164}, {'name': 'NML Cygni', 'mass': 50.0, 'radius': 1900.0, 'distance': 5251.0, 'gravity': 0.003798741848470553}, {'name': 'VB 10', 'mass': 0.075, 'radius': 0.1, 'distance': 18.72, 'gravity': 2057.0187109468047}, {'name': 'WOH G64', 'mass': 20.0, 'radius': 1600.0, 'distance': 163000.0, 'gravity': 0.0021427278239029217}, {'name': 'TRAPPIST-1', 'mass': 0.08900000000000001, 'radius': 0.12, 'distance': 39.6, 'gravity': 1695.1357895765334}, {'name': '2MASS J0523-1403', 'mass': 0.07, 'radius': 0.086, 'distance': 40.3, 'gravity': 2595.8411711966182}, {'name': 'WISE 0855−0714', 'mass': 0.003, 'radius': 0.086, 'distance': 7.27, 'gravity': 111.25033590842645}, {'name': 'Icarus', 'mass': 33.0, 'radius': 0.2, 'distance': 14400000000.0, 'gravity': 226272.05820414852}, {'name': 'SDSS J000013.54+255418.6\xa0[de]', 'mass': 0.045820224000000014, 'radius': 0.10173537, 'distance': 46.1, 'gravity': 1214.2000569364611}, {'name': '2MASS J00040288-6410358', 'mass': 0.018137172, 'radius': 0.16750369, 'distance': 192.0, 'gravity': 177.29553270309606}, {'name': '2MASS J00242463-0158201', 'mass': 0.075412452, 'radius': 0.11201167, 'distance': 37.7, 'gravity': 1648.517250730695}, {'name': '2MASS J00274197+0503417', 'mass': 0.029592228, 'radius': 0.14797872, 'distance': 236.0, 'gravity': 370.6432628229708}, {'name': '2MASSW J0030300-145033', 'mass': 0.051547752, 'radius': 0.10070774, 'distance': 87.2, 'gravity': 1393.9943359838126}, {'name': '2MASS J00332386-1521309\xa0[de]', 'mass': 0.027683052000000003, 'radius': 0.14695109, 'distance': 131.0, 'gravity': 351.5971318717637}, {'name': '2MASS J00345157+0523050', 'mass': 0.040092696, 'radius': 0.09659722, 'distance': 31.0, 'gravity': 1178.4549471797168}, {'name': '2MASS 0036+1821', 'mass': 0.040092696, 'radius': 0.09659722, 'distance': 28.6, 'gravity': 1178.4549471797168}, {'name': '2MASSW J0045214+163445', 'mass': 0.021955524, 'radius': 0.16647606, 'distance': 57.0, 'gravity': 217.27872675245442}, {'name': 'WISEP J004701.06+680352.1\xa0[fr]', 'mass': 0.011455056000000002, 'radius': 0.13359189999999999, 'distance': 40.0, 'gravity': 176.04104671648304}, {'name': '2MASS J00501994-3322402\xa0[de]', 'mass': 0.03818352, 'radius': 0.09659722, 'distance': 34.0, 'gravity': 1122.3380449330632}, {'name': '2MASS J00584253-0651239\xa0[de]', 'mass': 0.027683052000000003, 'radius': 0.14695109, 'distance': 96.0, 'gravity': 351.5971318717637}, {'name': '2MASSI J0103320+193536', 'mass': 0.049638576, 'radius': 0.10070774, 'distance': 70.0, 'gravity': 1342.3649161325598}, {'name': 'SDSSp J010752.33+004156.1\xa0[de]', 'mass': 0.049638576, 'radius': 0.10070774, 'distance': 51.0, 'gravity': 1342.3649161325598}, {'name': '2MASSI J0117474-340325\xa0[de]', 'mass': 0.01909176, 'radius': 0.16647606, 'distance': 163.0, 'gravity': 188.93802326300386}, {'name': '2MASS J01415823-4633574\xa0[de]', 'mass': 0.01909176, 'radius': 0.16544843, 'distance': 130.0, 'gravity': 191.292368446984}, {'name': 'SDSS J015141.69+124429.6', 'mass': 0.044865635999999987, 'radius': 0.09968011, 'distance': 70.0, 'gravity': 1238.4366334263514}, {'name': 'SDSS J020742.48+000056.2\xa0[de]', 'mass': 0.044865635999999987, 'radius': 0.09968011, 'distance': 111.0, 'gravity': 1238.4366334263514}, {'name': '2MASS J02103857-3015313', 'mass': 0.01431882, 'radius': 0.15722739, 'distance': 101.0, 'gravity': 158.86484308965376}, {'name': '2MASS J02340093-6442068', 'mass': 0.01909176, 'radius': 0.16647606, 'distance': 155.0, 'gravity': 188.93802326300386}, {'name': '2MASS J02411151-0326587\xa0[de]', 'mass': 0.025773876, 'radius': 0.14489583, 'distance': 152.0, 'gravity': 336.70141347991887}, {'name': '2MASS J02431371−2453298', 'mass': 0.031501404, 'radius': 0.10173537, 'distance': 35.0, 'gravity': 834.7625391438166}, {'name': 'LP 771-21', 'mass': 0.074457864, 'radius': 0.11098404, 'distance': 53.0, 'gravity': 1657.9311541328586}, {'name': "Teegarden's star", 'mass': 0.07636704, 'radius': 0.13050901, 'distance': 12.578, 'gravity': 1229.7078510792414}, {'name': '2MASS J02535980+3206373', 'mass': 0.06204822, 'radius': 0.1952497, 'distance': 184.0, 'gravity': 446.4014077055786}, {'name': 'WISE J0254+0223', 'mass': 0.06204822, 'radius': 0.1952497, 'distance': 24.0, 'gravity': 446.4014077055786}, {'name': 'DEN 0255-4700', 'mass': 0.07636704, 'radius': 0.09968011, 'distance': 16.2, 'gravity': 2107.9772483852794}, {'name': '2MASS J03185403-3421292\xa0[de]', 'mass': 0.046774812, 'radius': 0.09968011, 'distance': 45.0, 'gravity': 1291.1360646359838}, {'name': '2MASS J03205965+1854233', 'mass': 0.084003744, 'radius': 0.11817745, 'distance': 47.0, 'gravity': 1649.7053854867902}, {'name': '2MASS J03231002-4631237', 'mass': 0.021955524, 'radius': 0.17058658, 'distance': 192.0, 'gravity': 206.9336226190817}, {'name': 'SDSS J032553.17+042540.1', 'mass': 0.04295646, 'radius': 0.09762485, 'distance': 59.0, 'gravity': 1236.1885136462174}, {'name': '2MASS J03264225-2102057\xa0[de]', 'mass': 0.017182584, 'radius': 0.13359189999999999, 'distance': 80.0, 'gravity': 264.0615700747245}, {'name': '2MASS J03284265+2302051\xa0[de]', 'mass': 0.051547752, 'radius': 0.10070774, 'distance': 98.0, 'gravity': 1393.9943359838126}, {'name': '2MASS J03341218-4953322', 'mass': 0.06968492400000001, 'radius': 0.10687352, 'distance': 27.0, 'gravity': 1673.3068242582376}, {'name': 'LP 944-20', 'mass': 0.06968492400000001, 'radius': 0.14695109, 'distance': 20.9, 'gravity': 885.0548491944395}, {'name': '2MASP J0345432+254023', 'mass': 0.070639512, 'radius': 0.10790115, 'distance': 88.0, 'gravity': 1664.073567827919}, {'name': 'Teide 1', 'mass': 0.05250234, 'radius': 0.38844414, 'distance': 380.0, 'gravity': 95.4329811379458}, {'name': '2MASS J03510004-0052452', 'mass': 0.097367976, 'radius': 0.13050901, 'distance': 48.0, 'gravity': 1567.8775101260333}, {'name': '2MASS J03552337+1133437', 'mass': 0.01909176, 'radius': 0.13564716, 'distance': 29.8, 'gravity': 284.57813834448314}, {'name': '2MASS J04151954−0935066', 'mass': 0.02863764, 'radius': 0.09762485, 'distance': 18.6, 'gravity': 824.1256757641451}, {'name': '2MASS J04285096-2253227\xa0[de]', 'mass': 0.07636704, 'radius': 0.11201167, 'distance': 85.0, 'gravity': 1669.384557701969}, {'name': '2MASS J04351612-1606574', 'mass': 0.0954588, 'radius': 0.12948138, 'distance': 34.0, 'gravity': 1561.6306004391138}, {'name': '2MASS J04362788-4114465', 'mass': 0.037228932, 'radius': 0.20244311, 'distance': 142.0, 'gravity': 249.14464404913375}, {'name': '2MASS J04390101-2353083\xa0[de]', 'mass': 0.045820224000000014, 'radius': 0.09968011, 'distance': 29.5, 'gravity': 1264.7863490311681}, {'name': '2MASS J04433764+0002040', 'mass': 0.021000936, 'radius': 0.18291814, 'distance': 82.0, 'gravity': 172.14803783504922}, {'name': '2MASS J04455387-3048204\xa0[de]', 'mass': 0.061093632, 'radius': 0.10276300000000001, 'distance': 42.0, 'gravity': 1586.7166344045675}, {'name': '2MASS J04510093-3402150\xa0[de]', 'mass': 0.000992772, 'radius': 7.398936, 'distance': 69.0, 'gravity': 0.004973795867202517}, {'name': '2MASS J05002100+0330501\xa0[de]', 'mass': 0.061093632, 'radius': 0.10276300000000001, 'distance': 44.0, 'gravity': 1586.7166344045675}, {'name': '2MASS J05012406-0010452\xa0[de]', 'mass': 0.020046348, 'radius': 0.14181294, 'distance': 64.0, 'gravity': 273.3886765721481}, {'name': '2MASS J05160945-0445499\xa0[de]', 'mass': 0.044865635999999987, 'radius': 0.09968011, 'distance': 73.0, 'gravity': 1238.4366334263514}, {'name': '2MASS J0523−1403', 'mass': 0.064911984, 'radius': 0.10379063, 'distance': 40.0, 'gravity': 1652.6678012497337}, {'name': 'SDSS J053951.99-005902.0', 'mass': 0.058229868, 'radius': 0.10379063, 'distance': 41.62, 'gravity': 1482.5402334740256}, {'name': 'LSR 0602+3910\xa0[de]', 'mass': 0.026728464, 'radius': 0.14489583, 'distance': 34.6, 'gravity': 349.1718362013974}, {'name': '2MASS J06085283-2753583', 'mass': 0.036274344, 'radius': 0.15517213, 'distance': 102.0, 'gravity': 413.18933453695536}, {'name': '2MASS J06244595-4521548\xa0[de]', 'mass': 0.053456928, 'radius': 0.10173537, 'distance': 39.0, 'gravity': 1416.5667330925376}, {'name': '2MASS J06411840-4322329\xa0[de]', 'mass': 0.063957396, 'radius': 0.10379063, 'distance': 65.0, 'gravity': 1628.363862996061}, {'name': 'DENIS-P J0652197-253450\xa0[de]', 'mass': 0.07159410000000001, 'radius': 0.10790115, 'distance': 51.0, 'gravity': 1686.5610484742426}, {'name': '2MASS J07075327-4900503', 'mass': 0.068730336, 'radius': 0.10584589, 'distance': 60.0, 'gravity': 1682.5866846122526}, {'name': 'UGPS J072227.51-054031.2', 'mass': 0.024819288, 'radius': 0.10070774, 'distance': 13.4, 'gravity': 671.1824580662799}, {'name': '2MASSI J0727182+171001\xa0[de]', 'mass': 0.039138108, 'radius': 0.09659722, 'distance': 29.6, 'gravity': 1150.39649605639}, {'name': '2MASS J07290002-3954043\xa0[de]', 'mass': 0.035319756, 'radius': 0.09659722, 'distance': 25.8, 'gravity': 1038.1626915630836}, {'name': 'SDSS J074201.41+205520.5\xa0[de]', 'mass': 0.041047284, 'radius': 0.09659722, 'distance': 49.0, 'gravity': 1206.513398303043}, {'name': 'DENIS-P J0751164-253043\xa0[de]', 'mass': 0.067775748, 'radius': 0.10584589, 'distance': 55.0, 'gravity': 1659.2174251037488}, {'name': '2MASS J07522390+1612157', 'mass': 0.001918722, 'radius': 6.987883999999999, 'distance': 60.0, 'gravity': 0.010776994467105179}, {'name': 'DENIS J081730.0-615520', 'mass': 0.042001872, 'radius': 0.09659722, 'distance': 16.1, 'gravity': 1234.5718494263695}, {'name': '2MASS J08251968+2115521\xa0[de]', 'mass': 0.049638576, 'radius': 0.10070774, 'distance': 35.0, 'gravity': 1342.3649161325598}, {'name': 'SDSSp J083008.12+482847.4\xa0[de]', 'mass': 0.045820224000000014, 'radius': 0.10173537, 'distance': 43.0, 'gravity': 1214.2000569364611}, {'name': 'LHS 2021', 'mass': 0.084003744, 'radius': 0.11817745, 'distance': 55.0, 'gravity': 1649.7053854867902}, {'name': 'SDSS J083048.80+012831.1\xa0[de]', 'mass': 0.043911048, 'radius': 0.09865248, 'distance': 77.0, 'gravity': 1237.470248457338}, {'name': '2MASSI J0835425-081923\xa0[de]', 'mass': 0.059184456, 'radius': 0.10276300000000001, 'distance': 23.53, 'gravity': 1537.1317395794251}, {'name': '2MASSI J0847287-153237\xa0[de]', 'mass': 0.061093632, 'radius': 0.10276300000000001, 'distance': 43.0, 'gravity': 1586.7166344045675}, {'name': '2MASS J08533619-0329321', 'mass': 0.07350327599999999, 'radius': 0.10995641, 'distance': 27.6, 'gravity': 1667.4106478888941}, {'name': '2MASSI J0859254-194926\xa0[de]', 'mass': 0.047729400000000005, 'radius': 0.10070774, 'distance': 50.0, 'gravity': 1290.735496281308}, {'name': '2MASSI J0937347+293142', 'mass': 0.040092696, 'radius': 0.09659722, 'distance': 20.0, 'gravity': 1178.4549471797168}, {'name': '2MASS 0939−2448', 'mass': 0.030546816, 'radius': 0.09762485, 'distance': 17.4, 'gravity': 879.0673874817547}, {'name': '2MASS J09490860-1545485\xa0[de]', 'mass': 0.046774812, 'radius': 0.09865248, 'distance': 59.0, 'gravity': 1318.174829878469}, {'name': '2MASS J10073369-4555147', 'mass': 0.042001872, 'radius': 0.09659722, 'distance': 46.0, 'gravity': 1234.5718494263695}, {'name': '2MASSI J1010148-040649\xa0[de]', 'mass': 0.048683988, 'radius': 0.10070774, 'distance': 55.0, 'gravity': 1316.5502062069338}, {'name': '2MASS J10224821+5825453\xa0[de]', 'mass': 0.025773876, 'radius': 0.14489583, 'distance': 60.0, 'gravity': 336.70141347991887}, {'name': '2MASSW J1036530-344138\xa0[de]', 'mass': 0.046774812, 'radius': 0.09968011, 'distance': 53.0, 'gravity': 1291.1360646359838}, {'name': '2MASS J1047538+212423\xa0[de]', 'mass': 0.040092696, 'radius': 0.09659722, 'distance': 34.4, 'gravity': 1178.4549471797168}, {'name': 'DEN 1048-3956', 'mass': 0.07350327599999999, 'radius': 0.10995641, 'distance': 13.15, 'gravity': 1667.4106478888941}, {'name': 'Luhman 16B', 'mass': 0.041047284, 'radius': 0.10481826, 'distance': 6.516, 'gravity': 1024.6782379282668}, {'name': 'Luhman 16A', 'mass': 0.03818352, 'radius': 0.10379063, 'distance': 6.516, 'gravity': 972.157530146902}, {'name': 'DENIS-P J1058.7−1548', 'mass': 0.061093632, 'radius': 0.10276300000000001, 'distance': 49.0, 'gravity': 1586.7166344045675}, {'name': 'TWA 28', 'mass': 0.034365168, 'radius': 0.24560357, 'distance': 180.0, 'gravity': 156.25218516002334}, {'name': 'Cha 110913-773444', 'mass': 0.007636704, 'radius': 0.18497339999999998, 'distance': 163.0, 'gravity': 61.21591953721324}, {'name': 'SDSS J111010.01+011613.1', 'mass': 0.008591292, 'radius': 0.12742612, 'distance': 63.0, 'gravity': 145.11708292998327}, {'name': '2MASS J11145133−2618235', 'mass': 0.031501404, 'radius': 0.09865248, 'distance': 18.2, 'gravity': 887.7503956324381}, {'name': 'TWA 26', 'mass': 0.02863764, 'radius': 0.22607860000000002, 'distance': 137.0, 'gravity': 153.67219470602092}, {'name': '2MASS J11544223-3400390\xa0[de]', 'mass': 0.035319756, 'radius': 0.1541445, 'distance': 129.0, 'gravity': 407.69802411784036}, {'name': '2MASSW J1155395-372735\xa0[de]', 'mass': 0.061093632, 'radius': 0.10276300000000001, 'distance': 31.0, 'gravity': 1586.7166344045675}, {'name': '2MASS J12074836-3900043', 'mass': 0.016227996, 'radius': 0.17572473, 'distance': 217.0, 'gravity': 144.13720666656857}, {'name': '2MASSI J1217110-031113\xa0[de]', 'mass': 0.040092696, 'radius': 0.09659722, 'distance': 36.0, 'gravity': 1178.4549471797168}, {'name': '2M 1237+6526', 'mass': 0.039138108, 'radius': 0.09659722, 'distance': 45.6, 'gravity': 1150.39649605639}, {'name': 'TWA 29', 'mass': 0.001909176, 'radius': 2.569075, 'distance': 262.0, 'gravity': 0.07933583172022833}, {'name': 'SDSSp J125453.90-012247.4\xa0[de]', 'mass': 0.044865635999999987, 'radius': 0.10070774, 'distance': 38.0, 'gravity': 1213.291366504429}, {'name': 'Kelu-1A', 'mass': 0.060139044, 'radius': 0.10070774, 'distance': 61.0, 'gravity': 1626.3267253144477}, {'name': 'Kelu-1B', 'mass': 0.055366104000000006, 'radius': 0.10070774, 'distance': 61.0, 'gravity': 1497.253175686317}, {'name': '2MASS J13204427+0409045', 'mass': 0.063957396, 'radius': 0.10379063, 'distance': 101.0, 'gravity': 1628.363862996061}, {'name': 'SDSSp J132629.82-003831.5\xa0[de]', 'mass': 0.048683988, 'radius': 0.09968011, 'distance': 65.0, 'gravity': 1343.8354958456155}, {'name': 'SDSSp J134646.45-003150.4\xa0[de]', 'mass': 0.042001872, 'radius': 0.09659722, 'distance': 48.0, 'gravity': 1234.5718494263695}, {'name': '2MASS J13595510-4034582', 'mass': 0.060139044, 'radius': 0.10276300000000001, 'distance': 51.0, 'gravity': 1561.9241869919965}, {'name': 'ULAS J141623.94+134836.3', 'mass': 0.030546816, 'radius': 0.09865248, 'distance': 29.7, 'gravity': 860.8488684920613}, {'name': 'SDSS J141659.78+500626.4\xa0[de]', 'mass': 0.056320692, 'radius': 0.10173537, 'distance': 149.0, 'gravity': 1492.4542366510666}, {'name': 'DENIS-P J142527.97-365023.4\xa0[de]', 'mass': 0.020046348, 'radius': 0.13564716, 'distance': 38.0, 'gravity': 298.8070452617073}, {'name': 'LHS 2924', 'mass': 0.072548688, 'radius': 0.10892878, 'distance': 38.5, 'gravity': 1676.9544351685863}, {'name': '2MASS J14392837+1929150', 'mass': 0.068730336, 'radius': 0.10584589, 'distance': 47.0, 'gravity': 1682.5866846122526}, {'name': 'LSPM J1440+1339', 'mass': 0.087822096, 'radius': 0.12228797, 'distance': 72.0, 'gravity': 1610.6949805497954}, {'name': '2MASS J14482563+1031590\xa0[de]', 'mass': 0.056320692, 'radius': 0.10173537, 'distance': 47.0, 'gravity': 1492.4542366510666}, {'name': 'CFBDSIR 1458+10A', 'mass': 0.010595927, 'radius': 0.1541445, 'distance': 104.0, 'gravity': 122.30940954396387}, {'name': 'CFBDSIR 1458+10B', 'mass': 0.008591292, 'radius': 0.13359189999999999, 'distance': 104.0, 'gravity': 132.03078503736222}, {'name': 'TVLM 513-46546', 'mass': 0.07159410000000001, 'radius': 0.10790115, 'distance': 35.1, 'gravity': 1686.5610484742426}, {'name': '2MASS 1503+2525', 'mass': 0.042001872, 'radius': 0.09659722, 'distance': 20.7, 'gravity': 1234.5718494263695}, {'name': 'CFBDS J150411+102717', 'mass': 0.042001872, 'radius': 0.09659722, 'distance': 71.0, 'gravity': 1234.5718494263695}, {'name': '2MASSW J1506544+132106\xa0[de]', 'mass': 0.065866572, 'radius': 0.10481826, 'distance': 46.0, 'gravity': 1644.2511259779167}, {'name': '2MASS 1507−1627', 'mass': 0.05727528, 'radius': 0.10173537, 'distance': 23.9, 'gravity': 1517.750071170576}, {'name': 'TVLM 868-110639', 'mass': 0.075412452, 'radius': 0.11098404, 'distance': 53.0, 'gravity': 1679.1866817499465}, {'name': '2MASSW J1515008+484742\xa0[de]', 'mass': 0.054411515999999986, 'radius': 0.10173537, 'distance': 34.0, 'gravity': 1441.862567612047}, {'name': '2MASSI J1526140+204341\xa0[de]', 'mass': 0.051547752, 'radius': 0.10070774, 'distance': 67.0, 'gravity': 1393.9943359838126}, {'name': 'DENIS-P J153941.96-052042.4\xa0[de]', 'mass': 0.060139044, 'radius': 0.10276300000000001, 'distance': 51.0, 'gravity': 1561.9241869919965}, {'name': '2MASS J15462718-3325111\xa0[de]', 'mass': 0.042001872, 'radius': 0.09659722, 'distance': 37.0, 'gravity': 1234.5718494263695}, {'name': '2MASSW J1552591+294849\xa0[de]', 'mass': 0.02863764, 'radius': 0.14695109, 'distance': 68.0, 'gravity': 363.72117090182434}, {'name': '2MASSW J1555157-095605\xa0[de]', 'mass': 0.067775748, 'radius': 0.10584589, 'distance': 44.0, 'gravity': 1659.2174251037488}, {'name': '2MASS J16150413+1340079\xa0[de]', 'mass': 0.040092696, 'radius': 0.09659722, 'distance': 48.0, 'gravity': 1178.4549471797168}, {'name': 'SDSSp J162414.37+002915.6\xa0[de]', 'mass': 0.041047284, 'radius': 0.09659722, 'distance': 36.0, 'gravity': 1206.513398303043}, {'name': '2MASS J16262034+3925190\xa0[de]', 'mass': 0.067775748, 'radius': 0.10584589, 'distance': 110.0, 'gravity': 1659.2174251037488}, {'name': '2MASSW J1632291+190441\xa0[de]', 'mass': 0.046774812, 'radius': 0.09968011, 'distance': 50.0, 'gravity': 1291.1360646359838}, {'name': 'WISEPA J164715.59+563208.2', 'mass': 0.039138108, 'radius': 0.09659722, 'distance': 28.0, 'gravity': 1150.39649605639}, {'name': 'LSPM J1658+7027\xa0[de]', 'mass': 0.06968492400000001, 'radius': 0.10687352, 'distance': 60.0, 'gravity': 1673.3068242582376}, {'name': '2MASSI J1726000+153819', 'mass': 0.022910112000000003, 'radius': 0.1438682, 'distance': 114.0, 'gravity': 303.58098872536374}, {'name': 'SDSSp J175032.96+175903.9', 'mass': 0.044865635999999987, 'radius': 0.09968011, 'distance': 90.0, 'gravity': 1238.4366334263514}, {'name': '2MASS J18283572-4849046', 'mass': 0.04295646, 'radius': 0.09762485, 'distance': 39.0, 'gravity': 1236.1885136462174}, {'name': 'LSR J1835+3259', 'mass': 0.07350327599999999, 'radius': 0.10995641, 'distance': 18.5, 'gravity': 1667.4106478888941}, {'name': '2MASSW J1841086+311727', 'mass': 0.063957396, 'radius': 0.10379063, 'distance': 138.0, 'gravity': 1628.363862996061}, {'name': '2MASS J18432213+4040209', 'mass': 0.091640448, 'radius': 0.12537086, 'distance': 46.0, 'gravity': 1599.0828753069409}, {'name': '2MASS J20004841-7523070', 'mass': 0.023864700000000003, 'radius': 0.19319444, 'distance': 105.0, 'gravity': 175.36531952079122}, {'name': 'SDSS J204749.61-071818.3', 'mass': 0.043911048, 'radius': 0.09865248, 'distance': 65.0, 'gravity': 1237.470248457338}, {'name': '2MASSI J2057540-025230', 'mass': 0.06682116, 'radius': 0.10481826, 'distance': 47.0, 'gravity': 1668.0808524413646}, {'name': '2MASSI J2104149-103736', 'mass': 0.065866572, 'radius': 0.10481826, 'distance': 62.0, 'gravity': 1644.2511259779167}, {'name': 'PSO J318.5−22', 'mass': 0.006204822, 'radius': 0.15722739, 'distance': 80.0, 'gravity': 68.84143200551661}, {'name': 'HB 2124-4228', 'mass': 0.08973127199999999, 'radius': 0.12434323, 'distance': 113.0, 'gravity': 1591.7560663764139}, {'name': '2MASS J21392676+0220226', 'mass': 0.043911048, 'radius': 0.09865248, 'distance': 32.1, 'gravity': 1237.470248457338}, {'name': '2MASS J21481628+4003593', 'mass': 0.05250234, 'radius': 0.10173537, 'distance': 26.3, 'gravity': 1391.270898573028}, {'name': '2MASSW J2206450-421721', 'mass': 0.021000936, 'radius': 0.13667479, 'distance': 93.0, 'gravity': 308.3463412722992}, {'name': '2MASSW J2208136+292121', 'mass': 0.025773876, 'radius': 0.14489583, 'distance': 154.0, 'gravity': 336.70141347991887}, {'name': '2MASSW J2224438-015852', 'mass': 0.058229868, 'radius': 0.10173537, 'distance': 38.0, 'gravity': 1543.0459056900854}, {'name': '2MASS J22282889-4310262', 'mass': 0.040092696, 'radius': 0.09659722, 'distance': 35.0, 'gravity': 1178.4549471797168}, {'name': '2MASS J22373255+3922398', 'mass': 0.06968492400000001, 'radius': 0.10687352, 'distance': 64.0, 'gravity': 1673.3068242582376}, {'name': '2MASSW J2244316+204343', 'mass': 0.011455056000000002, 'radius': 0.13256427, 'distance': 56.0, 'gravity': 178.78094402431125}, {'name': '2MASS J23224684-3133231', 'mass': 0.022910112000000003, 'radius': 0.14284057, 'distance': 56.0, 'gravity': 307.9647729940028}, {'name': '2MASS J23225299-6151275', 'mass': 0.016227996, 'radius': 0.16339317, 'distance': 148.0, 'gravity': 166.7147684085729}, {'name': '2MASS J23515044-2537367', 'mass': 0.084003744, 'radius': 0.11920508, 'distance': 67.0, 'gravity': 1621.3847891693522}, {'name': '2MASSI J2356547-155310', 'mass': 0.07636704, 'radius': 0.11201167, 'distance': 74.0, 'gravity': 1669.384557701969}, {'name': 'WISE 0410+1502', 'mass': 0.005727528000000001, 'radius': 0.12023271, 'distance': 20.0, 'gravity': 108.66731278795253}, {'name': 'WISE 0458+6434A', 'mass': 0.01431882, 'radius': 0.43160459999999995, 'distance': 35.9, 'gravity': 21.082013105928027}, {'name': 'WISE 0458+6434B', 'mass': 0.00954588, 'radius': 0.3904994, 'distance': 35.9, 'gravity': 17.169284911753024}, {'name': 'WISE 1405+5534', 'mass': 0.02863764, 'radius': 0.08837618, 'distance': 25.3, 'gravity': 2.447107096961006e-10}]