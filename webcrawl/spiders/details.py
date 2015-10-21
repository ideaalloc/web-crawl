#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json

from scrapy.spiders import Spider
from scrapy.selector import Selector

from webcrawl.items import Details


class DetailsSpider(Spider):
    name = "details"
    allowed_domains = ["amazon.com"]
    # with open('products.json') as data_file:
    #     data = json.load(data_file)
    #     print 'urls'
    #     print map(lambda x: x['url'], data)
    start_urls = (
        'http://www.amazon.com/Crest-Pro-Health-Whitening-Fresh-Toothpaste/dp/B003CP12MA',
        'http://www.amazon.com/Optimal-Multivitamin-Chewable-Seeking-Health/dp/B00AERLWWY',
        'http://www.amazon.com/Pressure-Support-Supplement-PERFECT-PRESSURE/dp/B01635W3KA',
        'http://www.amazon.com/Crest-Pro-Health-Clean-Cinnamon-Toothpaste/dp/B003CP12K2',
        'http://www.amazon.com/Oral-B-Pro-Health-Toothbrush-Count-Color/dp/B003UZTF9E',
        'http://www.amazon.com/Health-L-Arginine-Supplement-5000mg-L-Citrulline--Cardiovascular-Health-Formulated/dp/B00J7UTCVC',
        'http://www.amazon.com/Liquid-Health-Glucosamine-Chondroitin-ounces/dp/B00DJHZOWA',
        'http://www.amazon.com/Bioavailable-Well-Tolerated-Vegetarian-Seeking-Health/dp/B004JGPSXA',
        'http://www.amazon.com/Nature-Made-Diabetes-Health-Packets/dp/B000LY3G7O',
        'http://www.amazon.com/Health-Valley-Organic-Multigrain-Blueberry/dp/B000EVNYQ2',
        'http://www.amazon.com/Pro-Health-Rechargeable-Toothbrush-Including-Sensitive/dp/B008CC3LWC',
        'http://www.amazon.com/Designs-Health-Vitamin-Supreme-Beauty/dp/B003CF7TOA',
        'http://www.amazon.com/Vegetarian-Development-BreastFeeding-Seeking-Health/dp/B00EKWVLC0',
        'http://www.amazon.com/Riboflavin-Pantothenic-Formulated-Seeking-Health/dp/B00HZUNQ9K',
        'http://www.amazon.com/Oral-B-Glide-Pro-Health-Clean-Flavor/dp/B001FWXSBU',
        'http://www.amazon.com/EyeScience-Macular-Formula-Advanced-Vitamin/dp/B0025YT6UO',
        'http://www.amazon.com/Glide-Pro-Health-Clinical-Protection-Floss/dp/B00FBQBPDE',
        'http://www.amazon.com/Iceland-Health-Joint-Relief-Formula/dp/B000ZWHBIM',
        'http://www.amazon.com/Designs-Health-B-Supreme-Capsules-Beauty/dp/B00290I4NO',
        'http://www.amazon.com/Designs-Health-Vitamin-D-Ultra-Beauty/dp/B0041RDVUY',
        'http://www.amazon.com/Planters-Nutrition-Almond-Peanut-Pistachio/dp/B005VOOT8O',
        'http://www.amazon.com/Crest-Pro-health-Multi-protection-Alcohol-Rinse/dp/B009XHNSIC',
        'http://www.amazon.com/Designs-Health-Vitamin-Supreme-Capsules/dp/B0054SHMA4',
        'http://www.amazon.com/Prostate-Health-Supplement-Function-capsules/dp/B00KHVIPGS',
        'http://www.amazon.com/Mason-Vitamins-Advance-Formula-100-Count/dp/B002VPE7VK',
        'http://www.amazon.com/Designs-Health-Magnesium-Malate-Capsules/dp/B004USSV36',
        'http://www.amazon.com/Designs-Health-PurePea-Natural-formerly/dp/B005JK3OOA',
        'http://www.amazon.com/Vegetarian-Broad-Spectrum-Physician-Formulated-Seeking-Health/dp/B003X5KGQW',
        'http://www.amazon.com/NUTRILITE%C2%AE-Vision-Health-Lutein-Count/dp/B003DH7QE0',
        'http://www.amazon.com/Nature-Made-Daily-Diabetes-Health/dp/B000CFIXS4',
        'http://www.amazon.com/Designs-Health-Vitamin-Lozenge-Tablets/dp/B00BMKO1PC',
        'http://www.amazon.com/Hydroxocobalamin-Magnesium-Formulated-Seeking-Health/dp/B00F4G45XI',
        'http://www.amazon.com/Health-Valley-Organic-Multigrain-Cobbler/dp/B000EVQ2O8',
        'http://www.amazon.com/Designs-Health-Twice-vegetarian-capsules/dp/B000FGWBM4',
        'http://www.amazon.com/Vibrant-Health-PureGreen-Comprehensive-Absorption/dp/B002L4X2BW',
        'http://www.amazon.com/Non-Racemic-L-Methylfolate-Formulated-Seeking-Health/dp/B00E0THMZS',
        'http://www.amazon.com/Designs-Health-DHEA-Capsules-Count/dp/B003ZVNKKI',
        'http://www.amazon.com/Colon-Care-Naturo-Sciences-Proprietary/dp/B00K5BCQHO',
        'http://www.amazon.com/Redd-Remedies-Joint-Health-Original/dp/B003SO1I8I',
        'http://www.amazon.com/Designs-Health-Digestzymes-capsules-Beauty/dp/B0077DOQQM',
        'http://www.amazon.com/Emerald-Laboratories-Adrenal-Health-Veg-Capsules/dp/B003XLASX2',
        'http://www.amazon.com/Philips-Sonicare-Toothbrush-HX6631-30/dp/B00QZ67NQC',
        'http://www.amazon.com/Life-Extension-Once-Daily-Mineral-Booster/dp/B00XWD91Y8',
        'http://www.amazon.com/TruNature-Liver-Health-Complex-Thistle/dp/B005KZISTK',
        'http://www.amazon.com/Designs-Health-Prenatal-180ct-Beauty/dp/B003YPOLRQ',
        'http://www.amazon.com/Vibrant-Health-Plant-Based-Superfood-Probiotics/dp/B00SK66JZ6',
        'http://www.amazon.com/Health-Kettle-Style-Potato-5-Ounce/dp/B001CX1D5U',
        'http://www.amazon.com/Heart-HealthTM-Essential-Vitamin-Single/dp/B0087SAIS6',
        'http://www.amazon.com/Green-Coffee-Extract-Appetite-Suppressant/dp/B011V0NZ4K',
        'http://www.amazon.com/American-Health-Enzyme-Probiotic-Complex/dp/B002UF94OQ',
        'http://www.amazon.com/Probiotic-American-Health-Products-VegTab/dp/B002RLFUVO',
        'http://www.amazon.com/Home-Health-Moisturizing-Hyaluronic-Restorative/dp/B000Q97ZS0',
        'http://www.amazon.com/Natural-Factors-Bronchial-Tablets-90-Count/dp/B00028OO52',
        'http://www.amazon.com/Crest-Pro-Health-Protection-Invigorating-Toothpaste/dp/B004V2MYOI',
        'http://www.amazon.com/Multivitamin-Vegetables-Bioflavonoids-Seeking-Health/dp/B004DSBQZS',
        'http://www.amazon.com/Crest-Pro-Health-Clean-Mint-Toothpaste/dp/B001G7Q05K',
        'http://www.amazon.com/Magnesium-Buffered-Chelate-caps-Pack/dp/B005A6964U',
        'http://www.amazon.com/Gaia-Herbs-Health-Liquid-Phyto-Capsules/dp/B00F1J7LGG',
        'http://www.amazon.com/Designs-Health-Magnesium-Buffered-Vegetable/dp/B000FGWBK6',
        'http://www.amazon.com/Now-Foods-Pressure-Veg-Capsules-90-Count/dp/B0011V1MT0',
        'http://www.amazon.com/Servings-Physician-Formulated-Seeking-Health/dp/B003800UXG',
        'http://www.amazon.com/Emerald-Labs-Thyroid-Health-Capsules/dp/B003ZUBZ9M',
        'http://www.amazon.com/Gaia-Herbs-Prostate-Health-Phyto-Capsules/dp/B00F1J8HHI',
        'http://www.amazon.com/Health-Warrior-Premium-White-Seeds/dp/B00B5BNN1Q',
        'http://www.amazon.com/Phytoceramides-Vegetarian-Dermatologist-Vimerson-Health/dp/B011Z7CAJ0',
        'http://www.amazon.com/NEGDA-Supports-cell-damaging-oxidation-Vegetarian/dp/B010RK2RCG',
        'http://www.amazon.com/Schiff-Prostate-Health-Formula-Palmetto/dp/B000UD8F5E',
        'http://www.amazon.com/Health-Valley-Organic-Added-Minestrone/dp/B001BM3CE2',
        'http://www.amazon.com/Designs-Health-L-Glutamine-850mg-Beauty/dp/B004037MNG',
        'http://www.amazon.com/Multivitamin-Vegetarian-Physician-Formulated-Seeking-Health/dp/B00TRLLUW0',
        'http://www.amazon.com/DETO-X-Capsules-Detoxifying-Intestinal-Guaranteed/dp/B013NSWXZA',
        'http://www.amazon.com/Culturelle-Probiotic-Health-Wellness-Capsules/dp/B00EEEITVA',
        'http://www.amazon.com/Designs-Health-Vitamin-D-Synergy-Beauty/dp/B004O51FM4',
        'http://www.amazon.com/Neosporin-Overnight-Renewal-Therapy-0-27-Ounce/dp/B0055OLROE',
        'http://www.amazon.com/Adenosylcobalamin-Mitochondrial-Allergens-Seeking-Health/dp/B00E0OXZEU',
        'http://www.amazon.com/Designs-Health-CoQnolTM-Ubiquinol-Beauty/dp/B004USC5N8',
        'http://www.amazon.com/Health-Max-Liquid-Gel-Ounce/dp/B006AWYKEO',
        'http://www.amazon.com/Culturelle-Digestive-Health-Capsules-Count/dp/B009CUTR7G',
        'http://www.amazon.com/Essential-Molybdenum-Formulated-Seeking-Health/dp/B00NG2IHB8',
        'http://www.amazon.com/American-Health-Acidophilus-Chewable-Strawberry/dp/B000M0IX2A',
        'http://www.amazon.com/Designs-Health-Supreme-vegetarian-capsules/dp/B000FH125U',
        'http://www.amazon.com/Designs-Health-Thyroid-Synergy-Capsules/dp/B000VYXBHE',
        'http://www.amazon.com/American-Health-Papaya-Enzyme-Chewable/dp/B00013Z13M',
        'http://www.amazon.com/Designs-Health-Curcumin-Vegetarian-Capsules/dp/B000RGC0GO',
        'http://www.amazon.com/Health-Measuring-Accurately-Measures-Circumferences/dp/B008CENXCS',
        'http://www.amazon.com/Metamucil-Health-Cinnamon-Oatmeal-Raisin/dp/B00NE64382',
        'http://www.amazon.com/Designs-Health-Oregano-150mg-gelcaps/dp/B000FH11TM',
        'http://www.amazon.com/Quatrefolic-Trimethylglycine-Homocysteine-Seeking-Health/dp/B0058PUJ80',
        'http://www.amazon.com/non-racemic-l-methylfolate-Vegetarian-Seeking-Health/dp/B005OE7IJI',
        'http://www.amazon.com/Advanced-Probiotic-Nutritional-Supplement-Fantastic/dp/B0105MVV78',
        'http://www.amazon.com/Designs-Health-Omegavail-Hi-Po-Softgels/dp/B0047OXWNC',
        'http://www.amazon.com/Oral-B-Pro-Health-Medium-Toothbrush-assorted/dp/B003USM192',
        'http://www.amazon.com/Designs-Health-Omegavail-Ultra-Softgels/dp/B002MAT5GQ',
        'http://www.amazon.com/Designs-Health-L-5-MTHF-Capsules-Count/dp/B004D3Z2QC',
        'http://www.amazon.com/Vibrant-Health-Vibrance-cartilage-discomfort/dp/B00SK66QXQ',
        'http://www.amazon.com/Optimum-Probiotics-Probiotic-Nutritional-Supplement/dp/B00WZ4VQ52',
        'http://www.amazon.com/Optimum-Colon-Cleanse-Support-Increased/dp/B00ISAPPLI',
        'http://www.amazon.com/Optimum-Probiotics-Women-Cranberry-Probiotic/dp/B010FX4XFO',
        'http://www.amazon.com/Dr-Tobias-Multivitamin-Mineral-Enzymes/dp/B00WR6JGD2',
        'http://www.amazon.com/Omega-Fish-Pills-Counts-Health-Supporting/dp/B00CAZAU62',
        'http://www.amazon.com/Phillips-Colon-Health-Probiotic-Capsules/dp/B007RA0ZAQ',
        'http://www.amazon.com/Immune-System-Support-Antioxidants-Mushrooms/dp/B00XJPDZH8',
        'http://www.amazon.com/Gaia-Herbs-Adrenal-Health-Phyto-Capsules/dp/B0036THML2',
        'http://www.amazon.com/Crest-Pro-Health-Advanced-Toothpaste-Packaging/dp/B005PLQGUC',
        'http://www.amazon.com/Liquid-Health-Glucosamine-Formula-Packaging/dp/B000VKA92I',
        'http://www.amazon.com/L-methylfolate-Methylcobalamin-Adenosylcobalamin-Seeking-Health/dp/B00822JNTC',
        'http://www.amazon.com/Supplement-Increase-Function--Focused--Clarity-/dp/B013PU6OEC',
        'http://www.amazon.com/Health-Warrior-Chia-Coconut-13-2-Ounce/dp/B008MIGHFE',
        'http://www.amazon.com/Rainbow-Light-Active-Multivitamin-Tablets/dp/B000EEBWJA',
        'http://www.amazon.com/Crest-Pro-Health-Two-Step-Toothpaste-System/dp/B00R2L69EG',
        'http://www.amazon.com/Probiotics-Billion-Capsule-Pro-Health-Naturenetics/dp/B00I3TFPCI',
        'http://www.amazon.com/Oral-B-Glide-Pro-Health-Threader-Floss/dp/B000GGJCDY',
        'http://www.amazon.com/Saw-Palmetto-Capsules-Prostate-Health/dp/B00XUZCSPC',
        'http://www.amazon.com/Crest-Pro-Health-Toothpaste-Peppermint-Flavor/dp/B00C18CK1G',
        'http://www.amazon.com/Purina-Pro-Plan-Urinary-Formula/dp/B003R0LM2U',
        'http://www.amazon.com/Trunature-Prostate-Palmetto-Lycopene-Strength/dp/B00F1MB79K',
        'http://www.amazon.com/Philips-Sonicare-Results-HX9033-64/dp/B00LM7S3PY',
        'http://www.amazon.com/Now-Foods-Clinical-Strength-180-Count/dp/B003P7YWDG',
        'http://www.amazon.com/Designs-Health-Twice-Capsules-Beauty/dp/B000FGXLVE',
    )

    def parse(self, response):
        items = []
        sel = Selector(response)
        # specs = sel.xpath('//div[@id="detail-bullets"]/table/tbody/tr/td/div/ul/li')
        # specs = sel.xpath('//div[@id="detail-bullets"]/table')
        # specs = sel.xpath('//div[@class="content"]/ul/li')
        item = Details()
        item['url'] = response.request.url
        item['spec_names'] = sel.xpath('//div[@class="content"]/ul/li/b/text()').extract()
        item['spec_values'] = sel.xpath('//td[@class="bucket"]/div[@class="content"]/ul/li/text()').extract()
        item['desc'] = sel.xpath('//div[@id="productDescription"]/p/text()').extract()
        item['pic'] = sel.xpath('//div[@id="imgTagWrapperId"]/img/@src').extract()
        item['comments'] = sel.xpath('//div[@id="revMHRL"]/div/div/div[@class="a-section"]/text()').extract()

        items.append(item)

        return items
