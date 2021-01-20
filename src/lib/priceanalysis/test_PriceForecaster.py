from unittest import TestCase
from ..priceanalysis.PriceForecaster import PriceForecaster
from ..datastructures.TestHelper import TestHelper


class TestPriceForecaster(TestCase):
    def test_price_forecaster_analyze(self):

        price_forecaster = PriceForecaster()
        test_helper = TestHelper()
        stock_info_container = test_helper.build_container_price_history()
        price_forecaster.analyze(stock_info_container)

        score_appl = stock_info_container.get_stock_scores("AAPL")[0]
        score_bngo = stock_info_container.get_stock_scores("BNGO")[0]
        score_ciic = stock_info_container.get_stock_scores("CIIC")[0]

        self.assertTrue(score_appl.get_score() != 0)
        self.assertTrue(score_bngo.get_score() != 0)
        self.assertTrue(score_ciic.get_score() != 0)

        self.assertEqual("PriceForecasting.ARMA", score_appl.get_analysis_source())
        self.assertEqual("PriceForecasting.ARMA", score_bngo.get_analysis_source())
        self.assertEqual("PriceForecasting.ARMA", score_ciic.get_analysis_source())
