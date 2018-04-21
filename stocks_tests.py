import unittest
from stocks import *

class TestDatabase(unittest.TestCase):

    def test_stock_table(self):
        conn = sqlite3.connect(DBNAME)
        cur = conn.cursor()

        sql = 'SELECT Symbol FROM Stock'
        results = cur.execute(sql)
        result_list = results.fetchmany(15)
        self.assertIn(('GOOG',), result_list)
        self.assertIn(('AAPL',), result_list)
        self.assertIn(('CME',), result_list)
        self.assertIn(('CRCW',), result_list)
        self.assertIn(('CEW',), result_list)
        self.assertIn(('CEO',), result_list)
        self.assertIn(('SQ',), result_list)
        self.assertIn(('FB',), result_list)
        self.assertIn(('SNAP',), result_list)
        self.assertIn(('MB',), result_list)
        self.assertIn(('CVI',), result_list)
        self.assertIn(('PGR',), result_list)
        self.assertIn(('PFE',), result_list)
        self.assertIn(('AXP',), result_list)
        self.assertIn(('GWW',), result_list)



        # sql = '''
        #     SELECT Symbol
        #     FROM Stock
        #
        #
        # '''
        results = cur.execute(sql)
        result_list = results.fetchmany(15)
        #print(result_list)
        self.assertEqual(len(result_list), 15)
        # self.assertEqual(result_list[0][3], 4.0)

        conn.close()
class TestStockAttributes(unittest.TestCase):
#
    def test_stock_industry(self):
        conn = sqlite3.connect(DBNAME)
        cur = conn.cursor()

        sql='''SELECT StockName
                FROM Overview
                GROUP BY Industry
                '''
        results= cur.execute(sql)
        result_list=results.fetchmany(15)
        self.assertIn(("CRCW - The Crypto Company",), result_list)
        self.assertIn(("AAPL - Apple Inc.",), result_list)
        self.assertIn(("AXP - American Express Company",), result_list)
        self.assertIn(("PFE - Pfizer Inc.",), result_list)
        self.assertIn(("CME - CME Group Inc.",), result_list)
        self.assertIn(("SKX - Skechers U.S.A., Inc.",), result_list)
        self.assertIn(("GWW - W.W. Grainger, Inc.",), result_list)
        self.assertIn(("CLF - Cleveland-Cliffs Inc.",), result_list)
        self.assertIn(("PGR - The Progressive Corporation",), result_list)
        self.assertIn(("SNAP - Snap Inc.",), result_list)
        self.assertIn(("ISRG - Intuitive Surgical, Inc.",), result_list)
        self.assertIn(("CEO - CNOOC Limited",), result_list)
        self.assertIn(("CVI - CVR Energy, Inc.",), result_list)
#
        conn.close()

class TestRevenue(unittest.TestCase):
    def test_stock_sector(self):
        conn = sqlite3.connect(DBNAME)
        cur = conn.cursor()

        sql='''SELECT StockName
                FROM Overview
                ORDER BY Sector
                '''
        results= cur.execute(sql)
        result_list=results.fetchmany(15)
        self.assertIn(("CLF - Cleveland-Cliffs Inc.",), result_list)
        self.assertIn(("SKX - Skechers U.S.A., Inc.",), result_list)
        self.assertIn(("MCD - McDonald's Corporation",), result_list)
        self.assertIn(("CEO - CNOOC Limited",), result_list)
        self.assertIn(("CVI - CVR Energy, Inc.",), result_list)
        self.assertIn(("CME - CME Group Inc.",), result_list)
        self.assertIn(("CRCW - The Crypto Company",), result_list)
        self.assertIn(("PGR - The Progressive Corporation",), result_list)
        self.assertIn(("AXP - American Express Company",), result_list)
        self.assertIn(("PFE - Pfizer Inc.",), result_list)
        self.assertIn(("ALGN - Align Technology, Inc.",), result_list)
        self.assertIn(("ISRG - Intuitive Surgical, Inc.",), result_list)
        self.assertIn(("GWW - W.W. Grainger, Inc.",), result_list)
        self.assertIn(("SWK - Stanley Black & Decker, Inc.",), result_list)
        self.assertIn(("SNA - Snap-on Incorporated",), result_list)


#
#

unittest.main()
