# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("eJzsvQl0W9eZJviwkARIcAephVqeSG2URBILV8mSRRLcCZAiuIjQQoN4jyRIbHoAuMCgLaechHKUmE7ZZSWxu1jVSZVd5XR7uip9nOmqbqc7maOku/oAGrjEftWsSaUm06U5Z+YwlWQqzZlzev7/PiwPCxfZTiqpQwDvv9t//7u++/577/cu/pYSfdRR86flpRT1JsVQjMRBWdCUOiinxCKVoF0GdplFJhGHSxxyi5yYWZYsYmZbsomZY8khpsKiSOJXWpTEzLXkEjPPkkdMlUVFzHxLPjELLAXELLQUxtJRChKKLEVgyh3FzhJLaTQ3aosazCxHmbPcUi6hXOerKPbASYqrklBSiqVmJbGiMtl/APY/jrvTwnNSw8cpl3yBWpSNUwuS/RL9BpRIYTnIKC2HmFzLYSbPUsGoLEeYfMtRpsByjCm0HGeKLDRTbDnBlFgqmVJLFaO2nGTKLKeYcstp5oDlDHPQcpY5ZKlmD7GH2Qr2CHuUPcYeZ+lpheUc5EM1ez6WLnsuOR+WC0rMadFsTTynh5M5ZmvjvHXAqWEqmCN/IAUOacx/TUtl+LB1qSV2HYXa00HtlVn0IKmeOZpeJ4zEor+hdykEc0ESq6FoysdSUm7IlPIfwPXHcdda4+48lrppytIEV/NT18bxPdZGy661QT9lbRz/pdVGC9TExbSaOLFdTexJ5iX2koG6dcDyDHtx7XImfvaZ1PLfP+jKqRLuFJlQbsjXlbR8VX6ifD3LPkvydZW9sk2+ru6eL8hRK1OVzAdS/8zyLHPS0pZ8B05TzKnfl6Tche3MaYshje9MGl8H4emMl/0sU53cB0hf2k1KF3PO0p0i6TxzIUVSD1Nj6U3hqmXqUrj6Ujg0jDaFo5/RWYxs29coRs+2A61nDV+j2A649HB1gU8D2w22HrA1sr2E9hHaT+IYv0a9XWoxsc3btI8prX3+nLRHU4b2GGCaM7RHS4b2uPgrbY9Lv9L2eOZTaI/BbdtjcK/tsSq55YQ75LLlWlotXknJc/uuHAbm2bTWuMBczdgaO8lJbYezTGtqO+zKkdpK6Rx9TJuln70GtdxOatZAalbUBtgC4J/aBnpsg7eLLUPb1v5Qau1nHIEy9fj2/RHo0xqBViX33YzhZcpiTnlWdXyiZ9Vwii43nFKrIykznk7HqHPMMvaUs5+YZnzdcp2Y45bxJE06pnnHNGmLxZKkccc08b2mF+OLhcc0+BuWG3F9/CYpQ7JuHouHevsuenGMP0Un79pFZ+9Ou5fS8yvMNm9JEjPP22lyejKkU8/0pvom5iGu06AbToBueCzK27dLTvt3nF0YoSc+F5VebLGmSU/rvynSB3aUPgjSJ5Xx+ZKrIjpHKk2Tc22XWd0Q9FebxZahzwpzs8QsLtZHY30t1jcZC0NM1sISc8oyldQHY3031tdi8mJ9NxYekxPr+9OW6Yyzy9T0hT6b4IvJj8mL5Tt278TkpPLH5MXkx/iF/An3wQypI7OjYBjNYYfKabfYid+II9c5a5lL7pNgH3VkOR0WR0rdCnkSZJaQNithxt67njJSOeOjjIuhLG6GsnrAvAMXN01ZvXD5QDv3wzUP1wJci+C3BOEBsD8PZhDMZVY5+0JMUuaZEjOedtdZLC8yN2D2e9Nyl7lleYm5bfkMM8E8x1iZybdklt9ibJaXlUJf+2wsFvsyw7zHJj8HYM6VNp8Qck5KM2X5HDMNffnzzAzQFcYO9B4zC/QVZg7oFxgH0PtSqotinC9TjCvlKfNFxg3hX2I8QF9l7gBdZTigr0HOZhhvao02UJYvs19ei9er+MO+llYHEvymloeRmKkqSkt55QtSoURYOkk0pNr3BNlM1RI+27vk9bFOsMk9Vt8MmCXDMxxrZQbdbkfHImvz+9wc+Ba2u10u1uazu10dHOfmAg0eu4e2u7w+q8NBO1nbjNVlD7A0x97xs16fl57y+/wc6718WUdfoesYdr7O5Xc4AvmeJd+M20VzfletZ6k6K3DA5nbWTllt7KTbPVdrZbxOq8s6zXJbxUkBDruPTfFyczbrVmmS15zVB7EDJUmeThI3p+KG9lJLkzMgWLQxiy5m0ccs9TFLQ8zS6AzIK25oYk6wKNCi1TTFbY1xW0PcVh+36eM2XdymjdtAXvuMz+fxXqyr46wLtdN234x/0u9lOZvb5WNdvlooT92Q1blodUH5Zqx1DJSzzmm1u+o8nHvRznprfYu+gLIWXWjlJQv+A9DC0WLc+NHKV2/R/QOthh5TV21tLS/hAnmimDz18TPg9XF217SQgSsfV4jfivHtK6UUVa3YOmZ0B+wOh7WuoVZDn+23u/yLl+iRS3Sri+HcdoYrgJJtVWZiinLQjbWaWu2lrbWdeLS6S7TZWGNu0TSa6Da/3cHUXRvUttZqWzRNWm2tRqe5RC/MV9OtHo+DHWMn++y+ugZ9U62+kT7b1z1s7L9AO+xzLN3F2ubc1fQoy3nh5qirh6TaZzi3k61r1kA29C3NTbVabQttdE/aHSxttk5ZOXtU0tYXdsyhhuSwq6WlceRTzmHGzPzunjLTrOn85VRXUzOpLk19bUtj5gyu7JRBjB3LY2M8j0PaRtPYnnMVzUmjDnOi0+hqm+sz5+TBTjlpiudDrxltj2bENGRo0Rg/aR01kDrS6Fpqm/UZc1ZdyEv0vKSelzTwkkZe0sRLmnlJCy/VauDSwqWDSw9XPVwNcDXC1VQt28qjWVeN33uJ7hquCfyz3e6cQfsi66Abo4UzG6An6LSaZi2UXaf/pKVsAXttfaOmsbZJm7GUga/sfvdHW6DBHM2j0dima+n7xA0ACdbqmpv1tS2Zs1Z9mJe08pI2XtLOSwy8pIOXdPKSLl7SzUt6eEkvL+njJf28xMhLTLxkgJcM8pJrvGSIl5h5yTAvGeElo7xkjJdc5yXjvMTyBJ/1T/6bjKICtU/Xi5/0YEwGCC/R2GeKKMp+EgbYJ2fR+3coHGoD6kxFIAMsV4ikCEkxkhIkpUhwg21LQm9JL8FVTW9Jau1FZ1CaEGX3yNU53EG0H0JyGEkFkiNIjiI5BiRwPtodceAZronm07k07PbbZmh9F2122Bk22raBi09XNc0t2MH0YLS0QC2UptaCvla7l3IoAieS+qF5yTlpt7rq4AYwsxw8XBs1dXuQ80SJwmR8lsk9Z7cG3t55bNFi3+5q1um10cLXa2t1ta3YLbUtn7h7t5DxpQkS0TVkvvXe3e0p0eV2T0MsYYSojz0rDMKzolkHzwptfW277tN7XMC4kzGrTwqhWz6RCy2V1sYNe2pj7iQQm1gFz4ML7kbqpxEJ7i/7JIkgnyxhn41r46CfS5P182QdnpEFMO7ucuRM1k5yUAqTvUdZOYxiN1nL28VVMrnJcZclTN6ylFFtw5/PFCTzf41iCpN443afIuGbnCOIU7SN/GKmJE1+9ja8pYw6jbfsbWVQSkosC8pgdlRu4trAZX8bRGxloVpRyz0LHk8wcxyOqpwBSQcy3T3sOWj/H8xfHA389Y3OtlZTXWdbfeslsI3W1euaSGS9trZRD15t4AUfLcwCtOA0GOueZ1iX1+5bugwKx4UFO+Obudyk01yYYe3TM77L2vqGxmVg7G+vY10TI2awDo3W6Zt1mmY9PNjA2T5U12rnfKwD7MbOuoHBwQFMxxCzDZrqMsyPMO3RuvbBbm1zC+bLPFrXAsbAYB1mq721zso5WeukvWa+yXoxar90K0AbrI55+1ydDoagTHo5zRmxkvKxarqwD6nEeqI9519JKPuzbYXUEzdyXEXSDaQ6i5fBJILP5qwuxu3kc9C0u3x8tm3GbbexfLbTzbAOXbWcz5m3kXufl4+2Dg7ysg6TgZf6rV68xWn48DKr182rUABJud/cxt2CsK/A5T0LXekutVFQ/Mbp12vXStfM4ZLqSEl1uOBcpODcO03hAt239N+a/9MXPrQ+lISbeiNNvWF9X0TfFy7oe9geLhj4aND80bAlMjwZsrGhKXt4eDYyPBsenIsMzoUL5u52beQV37/yoHqtJ5xXG8mrvWvYlFJ5c7K77WDm2qTf7HzP9IH2g6HwhauRC1c3KfQT6Pc6v2v8aOh62DAeMYyLAz6adkam/aH5IDhfkBikP6GoGUmH9GeCIeb8OUV1S00Y0i0dRb8xqQWNG9LbGKtbOiGETSTFilNGOo1sudPSu23refl3e35KxoDO3adzRrfXyrmnvHarc24GnnwjVi3O5IRZ3Yh1wscu+qolfI6fc7g9rCugADG0BxcCcp1zjJ2jzT2tRj7L5mCtXEBHxz4VN/TNlxou1Tc66bGO/vYBYwc9PED3tprpsYGhfkOcjw5U5NKxVQiYhtJDseUHmOXmBtTiNYrYykTSYJ5FRQfz01l7G8yTF96Th6htY8ftO8XeceCW71XCMjxu1rKoDJ9gCvdadiYuRpq6mLQNn4yR74kvi8neE1/aA2lZ4itMhM/GHwzJNQAPI+qz0kMJN8XkprgpJu+zsoTPmjJT+slSk1LO3SZlVVrKHyOlQGpq25UTHqPi1EhbS4PSbWqzYI+tWLhHvqI98hXvka9kj3yle+RT75GvbI985XvkO7BHvoN75Du0R7693qV7Le/hVL5lGSNZlgflQQn2tCBRUZezglmgHlWYOHzG85IJXqZv1PCy3usw2/WTSRwvsXKnwHyCmvWTMiT/Az5PcETiBpHgduyWpGZLUrUluUiUqS1J9Zbk7Jbk2S3J5S3J+S3JJV5yLiCl6eo8zowypW4vnzPN+li/neEVYHG4p+0uPhts6COfdYMrh2M9DtBzeAUYvik3B5rEvDBr4LP8Hg/LIQs8Z7xsdTb4QEyGl2J05Oelix5eNrnI8NmTficwe7GehGcMdxMzgan1sUscbiR8Hy7vX0pRn/ixqvAN6eu5r6leV4VVRyOqo9+QfaPt632/Z/y6MUzrIrQurNJ9y/znJX926NsVf1YRbuiINHSEVR13O9aVea8eeOXAatm9Y/ePPVYef6Q8viZbawsrz0SUZx4r6x4p697Pep8NK5+JKJ95rDQ8Uho+ND8sDSuNEaXxsXLkkXIkNDoestwKK29HlLfvtm3klUbyKsJ5RyN5Rx9MPrA9sEXyKtf0a21r+kjemXfk8K18Rx7Jq3mcp3+Upw/nNUTyGr41E2nsDDd2Rxq7HxY/LHlYEmnsfzgMX+7hcKRx6HHj9UeN18ONlkijJZxn+eiGLXJjLnzDGbnhDLk8IbcHaOTGnXDenbuGdWX+q0deObJqe6ALK49FlFCo04+Up9e870Ch6iLKusfKpkfKpg9koAMpr0aUVx8rux8pux+WPpwMK69FlNceK8cfKbFEoQlrWDkZUU4+Vs4+Us6G5lwhDxdWeiNK72Pl84+Uz4eCL4LW0iYlKlEu0YiA/gNQo/TvCYVgk/QaGmbpCOEaJVyjhOs24bqNwRPSSUEDmopqQD8jFLnchMuNwR6pFw2/dIFwLRKuRcJ1Vfb3hEJwq8yARqesW4ZcPbKfEYpc1wjXNQweko2gMSYbJ1wWwmUhXJOEaxKDbbIpNGZks4RrjnDNES4v4fJisE+2gMaS7HnCFSRcQcJlkP89oRDcIe9Bo09ulCOXSf4zQkHXy1XdbV/PL1otuTe62nZv/G7nel7xXSN3G/p34HCyZhXdzxEUq1KxYhUNsYn0FQr1FaJXPaBQr1LiJJhy4KgiXZbDlSXWboLRKbAw1kTtZEKWrLEsZzMwIsGELett2XJOMCuYzWS/JV1WSGF8SmhowZyg4r2ctA0xCjfECHQSbMKWWLXCxCELGc62JMHAkZjCa/XYa2FWxU5zVmetm5uum3T7Aqo6L+tijKzXa51mq6V8jm3G6pvAESSq5WZ7rMDvrZbxipiyKQxgMhg7qpXcXTKYeby83Oaes3NfQGeWzz3HunCuY/WBqCz3HEqUgb7MvYKjjDI+DMVHoqwO3NDifhvs/xVZPkPhQLQpVWblrysOrBTid72oZCVrvbh0JXujsGRVt2p7rfFB5WstD8yvXV5Th0tPhQtPRwpPA0vB1XdGQgVXhd+KbP1oFbiL9fBbyV5XqFcU91Wr5rXykOJsWHE2ojgbiv1+sSmVYIKqFfmK/Be/+IVXBdn4TCvVKqe+I5e2KmWBE5l3CEW7gViJUY2dm4Do1RLOJxgjxOCzvA6W9YAll2FhuuGBbuZ9gtrSuxI+z2ldnFhwc3MwWAdyK27pYCJq7unMETbp9E3OQF50GgHzZSdwxOcUCXtzdEtPr3cGDiT2HhMTZkg0cLaSrDjZ/c7KS/OXK7WapsoLdKXJ7bvc+mwbzjWJt66+kpe1NGug9eXdbq9vS+llbTW2mRq/datg3s4ueNycr4bM8QMFdV7GZuWYOuPQRZjUDEMBFeyi3eubcM/5/zXcGbnRrUk6NxfbPZcWfSbwI6YTMYa6m4QS3+AEsgYF9qDAUEfTwBGkz5I4YCFfYicMdSgBOG5i+M0YA43xCYMgGULQqIaYQeES8pVL103UoeXmxE2SrbrghJCTOMPH+OROPPUH6ixWfTT9o995Ca7PwPVbcH0Wrs/B9Xm4VgiXXuvEXkObW/u6W009sYgYLLB9Lhrtt6JiXvo4pRCK8qPX7/4a/uJ9bWDBxXL0RXGWxVVDxxk7o3dHMq9xiDZ0jPb0J/jGYEzzWj2eZD6Nvl7bpNFpWvSaOGd0eTfK2FCri4eYfVaf3xsNGORYvA1/XWsyaWVBFnsCnqRSVxYYSTp8DPRqqennX6Kie/Y6549ef+nX4YeDsIezu3zvUkQtiD6CQCVgF7l/DnY9FMNbTR5BG4p8UDMKJ1FHUtpQR1KS5aUUSuRkrqvRtLoSgcTSas0nWufwieY129Qu9xw+VOScH4uByXG/h2WRw2zCzf0+uuMFJKyENGDxTgjFk2e/3LMyHZaXR+TlIXn5hlz5xZMv9b3cd5d8hWJJE9mgFLFifS5tpyB1MYaRzBGFyFuaxCXJzMV9Vaw+MdK0ihGHynYMlSdVonj5adsKTVl0yk6v8KQUsrZLIbV0e5ArWlBJf6/KlyfKMSVePBG6AOkGOYLKtyXJDQzGHhNRQFAU6oNAn+EZlm53uF2o+HZbvXQby7rodlBAHDALjfMlYulIrICaHh4Ybu2nB/ouxmSf8sZ92wejvo3oe2wQlRmadYEqR/vc9KTVNke3eu1TtJF1+WmYo8ocrIt00agS6Z7z8ll2l8fv4+WgLfhAe5IN9Hl5mc3j9WKh4lNVkOx3+Lh/AY6r2H/fokj/zcld0b+0+PLiqvYzy3eX35Y9aP+K4i3FWutX8x/kw727wtzLu5+3kgfWUMFiWLEUUSyFFEvEeeabVd+0favq3Zn3Zt6tea8mXNAUVjRHFM0hRXMi/P3tw2vDirqIoi6kqNtQqO5l389eId/NfOrQ6Qf5O4wI2dJfxogg5stw+4hD028fcah8x9Csp+nAyzgPypkjAwhXtFtnBl5FnDd/V15llPfkNjWZm5ZT0ZpkJplJ5cxLi10sSiVeZkaVxleW4POVi1LMNILnCyN4oCmqvWvhRroRvc20Ir9bou2DTtzyjd7JAUOGiDpxRNG2Q8I6RLal4sNBoC2DFP2uUtrdLp/V5qNbGafd5f8jCp/zaWJ+9OaryYJ+PTQB/8U9ZjdWWHNHf0f7MG3sMI2A5sZLtLxEx2FTBwYXmeka3AmiY1PthYWFpOkWIhqnoNVqPTOeZ+3MZa1Go2nU6zVNzZqmBk3Daad9EmbbEGCZHOtb6MdlCjPM1KFqxzg3tI/bgxhVXKagn2Cfr1alPPC5byDBFuBVTtY342YmbBwMvry0zcDLnTD4woTe7mS5N5BFTjaosmEKO8cuEbwsScyLnVMYbrlvxUg3jrW/oHbRFcAayh0My69F5NdC8mvE+VxYbo3IrSG5lThvh+UTEflESD4BTlCa8gy4vJPVgcs7QDcJ3cgvCZXeCOffjOTfvNu5npO/KvtM8G5wQ6G+V3C/YIV815WFq1WvHFk5sqHIvSe/L18h381sKrco6p+jfHkpVGwL5zCRHCaUw3zE2sPsXISdC8V+P8bx+3xYcSGiuBBSXIDx+37uqvZe/v38FXhqqL44ek91X7VCvunjOFYTGcdxE+VNGLFxlCPaWOC/pG6X6/SNZLu8BVEdwnZ5o16jaW5u0bZsu12ura9P7JfrmjXR/XK7b6JnWNgv12obmjUt2nqtsF8e3RlP2y2nWxv0zt23zHU6fZOwZa5tFPbM6+N75o31NfPN1ku3iDJZLeFugCHqKHyW37q4uMj9G7Dfwq5SSAkLN5TCJotuvO7wJDwiT30Spo7LSWpX+rPxU1MZd1b3dgxNV9rEoWmvwieFKp4yz+InlDLDszY3+kxsE2sKa3IqwyfDE27b53PmHRZfgYg/w9MN8qN6ivzk/wryU/AU+Sn8FeSn6CnyU/wryE9JXP8SaTsZdSVxPy1Ny1lpIjSx18yo0/gO7JxKdZlpjw9qOsOTerh7wODv2VN0kX4jxKNbHQ66x0z3mOjBoYH2DrO5x9RFc2sgzW9MExmLvJ3KZiTPZDotbZJejdZv2lbidrrcThJBpG4HkfqPkUkQqd9BZP3HE1kf0GWWp9lGXhvoNP5nnrJFo6pUNC8Xae59EMDnCHpSK/c/iVxtRKOLudq5cpHLwLWDK3AoRTcbiOtm3L+iiGr2HBXTyv5IFN0LCpcHlESGz0UgUVQ/yyKGsIsiN9utTu5fY0RU07g/och+Qbag/Ym1sz+JkefwkftXErJpK1e+1PVy190uom0NheXmiNwckpuJ0xqWT0bkkyH5ZFT5IhCqLIKgyiIAKqCE0xGWOyNyZ0juJE5nWO6KyF0huWsPzr6wvD8i7w/J+6OpTJBUniOpPEdSeU5KVLxb4fzbkfzbSSpe4asFrxSsLoUVJyKKEyHFiQ1FCWphjxWHHykOv60LK45FFMdCsZ9IC/wNiihaJvhxdl5IdTacXR3Jrg5lV29k5748u1r8kvNl513nRnbJS66XXXfJN7MCip+fNlOoPrGURcJQFikjeZmyyBgpUDkjA5rFyIFmM1lAc5hsoAomB6iSUcDQquT+AwoW6V4Ujv1EL1MTwdPwRJhIjPIwHr8rMYEOeFfomHKYNkyJdUHFxITdBVrqRKA00cVrY54vYV/FWf1dCnfy5PdzVuCbvsIY32btT1smeUrlcIcFEShYPK4yaQkjKIa2JcXJDEHby4M3mQfSzknY1xS7x4ht9fpKEhwnKe63d1UXRUsRs3FlIYOye0jEF1942Vnt9R0R5fbp1OO95uq4KAUqqZaLqAyf1LXX2MZ47J3r6hyTf5h6Sm1g0O+jyYIL3bFoxbVSGnjp2F4nrm0iNpT2N+9RcHS3CSUOWn0zRFrg/Jibg0eJ4EvgPLTN7ZrirE56ye2nORoXD2jWZ4s9ZYRFo/xhbolunYZbDR8/1cWpTx45RuPluDTBy/H9Vz7X63HYfbjR4Y0+czxW7wJfjCmb3L5Ot9/FkFdhRY+hxEoDWWTAQYP7LpBqKfcDtKMc8VItCQwUiUYAQn8Lb/+fU+RRpci/l4O3P1lG9YQVdyKKOyHFnQ31odDh58Jqa0RthfFBuSnNVVZtlB9+UP9Wy2vu192Py889Kj8XLr8QKb/wuLzpUXlTuLwlUt6yYrjfta4qerXnlZ57fff7Vsj3FxuF9CaVo6xKkA1Vcajk2bDqakR1NaS6uqEqut+7euee8b5xxbihKrjfszodVh2LqI6FVMeA942TgjSwrtaFVZURVWVIVZkSq/xe//3+x6pjj1THHnBxpvhvsxDSRSQBKsR/0lrclk39++y2Q4Yq2XcrJUBtYlUf7zwy8p0rFAAmPlFgYmFzTTxaxj+MRDyFEI9ovtyEPfkOmZJm3JHInOoeRrZPFpeRZgaNpsNyES6zDW82k/NJeN/OXpZvwy1PBfOCZOU2vLkwud5rLlQw8U3NRdZylngKtU3MApii7vC+y3L2pyAjJzNsmCmC6WhSPKbka/JlRRJ3fGyfhili6qk4y9vVnZopS4Ft5m7DWc4cSOHM2zb9g2npq7blPZTGm78t7+E03oJteSvSeAu35T2SxlvEHN1De6b1vAzvUykJQHt3WceY47vKovco6wRTuausKgLILQ5K11RUhg9zMmXnODuhtiyXKKk9x1OJ4pW6lAihC5YslyZOygjKDNSq/NYby+qgei0/o8xTwZK1gkwhKS8zJAOVM8s6HSzZE9+ZYOmnlubZYOme+KqD0j3xnYPaf+q8LZeJdbzZosxxGqjlcjvFnE/qZVWieCWZ4yW3+m9LmAtMDdDaTyynjtEA1X5iObpPLEHP1ANtYBqBNjHNQFuYi0AvMc8AvcxcAfpsUAL0arAMaCvTBrSdMQDtYDqBdn2yPDDdTA/Ty/Qx/YyRMTEDbym/IVk+QF4boVLhqq68bU5vGVwT5SHxYa69TAUPrKkzhSXnybBjHpcPQu8ZChZDac3MMNARZhToGHMd6DhjAXpjDyPYTebWTiMYSLn9qUiZ2IOU5xjrLlImGRtQhukGyjJTQKeZfqAzjB3oLDMH1ME4gboYN1APcwcoB19vUvrimfHBnbAtjO8tObT9oWD5mmh+l/gw/uCB4CFm/r2FPwCd94/jeu9aeSbu5PZcPswsBg/PU6sSbphZ2qa3BKC3HGaeT4ztu/SKCl9dIvbswXiJ9SLfw3HpwZ3Kvlaxexm2GTeXmRf2NL6+yNzdE99LzGdSxtgjzG8Fj4D+uRSsAM1SvnzU1yLif9l3MeECrs8GJUA/FywDetL3TFLY54mEdFjFswmuoCRYFqz4A5jF/LFMxCGagazRmfKdPnf3tYtyucLcSyl9xjlQUMK8QoD2ZUSf+EI63D5F7v2PJVewH90+DRjrFpgvQm/8kuhVulcT9nmKY5NaYZXU+muZav3t9PUTQyL8Y9Xmlz+92lyV338DrjfFc09GFYC+aZVF16yOJUJm48+X2ZMx20mKq5DgOtipzHkISoNlqf0pZV3nt02By/n5sbWV2NIL4nxrjNqo6xZ9yksHYzsRA30Xa8Adc24pkl/3xu4qvBNPXqXoRb/3odTcANpQTX+CC7LCC/QPkdz9nQfUk//xw59n/Tchj0VXo5aTV7dktdqpd7O3ZLpazZZcV6trQNrUsCXTo4cePAJyPd3U8CQEqT3BVcYnzTA8PqEgG+8W8lmz1oneQT6LXZwwXgfDNdE+QowRM581xU10DoHLO9EBLo9vog1cDDth6OCzCF6A+z8p3KWfc0/0QQjnnxiCyIGZiXYTn2XlJlo7iKiutmo5r+rirE6WdXlm3C6Wlw+5J+18bpvVNe2wOuyuOV4xzDpYn9Ux966MlyPEAWkDoY2t78o5fFRw+IwKFDtZr5d1TbNcjTV6vhWueEK8ErPbtdTB2W1er9tlHtY12Of54jS/gOK6h+XsVnpkqygVUfFkDOqG6wdxW9kCoOJJ18+KqCcvQgsEfnQpDYDRoicADF1Lrb5ZK0TQNzTompt0Lc0pCAx9AoGhac6EwCAtISAw6ptbmuqbdPrGXRAYQ6zLvRcERuzQAq12OwQGDUL76rTkZUNoeDvn9fFZncSQO6xI+wk1WfEwARehVsbO8Nn44qAVQmahfnklw87bbSx5I8fmcfByH+dn+aIpq9PuWJpIBB7wsjY/x06kBRTZOBZqzGe3OrwTviUPy1dEAyetXpaZIC8yTnisXu+Cm2P4YhbXEyG+z2p3CPzqSb/P53ZNLNh9MxOM3WuddLCQTa/bz9kgK1abze13+SY41uaeZ7klPs9rd054sUM4vFsHb5xp1rQ06esb9HDptJqm5vqmluYzt/g8XOi0MxNTDvcCnx/teEJ2+MJomIdzz9sZluOzp8mJLtD7nZAvXhHPrwqSh947Qd5h2qrRN2gamxsa9NomXXOwUTfVbGNbpprqJ7VgrbdpdXqbTaev1zdZ6616HX9wmnWxnNXHQna9iP6fsEFr21mvsOdY6IRamLC7piamJtHK543qJkZMw61dXR2Gv/l/YIS7cYZd6p2Z7LLZB+y95pFAj9Zk7/H2OH0eS3tPY88sMzswZtQPdI0ExmdbFyzDnXYwG4zOa0smg2V2wDCtH5/tWDTO9iyMB9DOzBlnW+397b0a9noryuwb1V6zT12rhWQ8Nr0RvFrt42Om2Un9qJ/pNvotupZ5i27R0e80zU+aIen23hnW1Ur4jMPjDSC6wRiYXjIuaRYtLrfG1jU6O9A13WDS9XrHnYtOmNRoBgwzOlNX8wI71tswrvN42bFx//j1tgXbUoNrUtfimuwa1dp0o0vjuhY/0wXptjfMTuo0kE3Iy/XRuZ5Z93TPbIduYLhnaWDYWG+cNfomDTN3LIbWhoGumYZxPQPpOFwWw7jGNNawaHQyTvb6qGZ8uBPy3+nud3Yu2ERlYa6bHDYsj2vIMem65od0fT32hekel0k7bodqbe9ZNBrmFo2BuXpTwBgwGYwLpmHbgtHQ0WAKzJF8Wca0M9axhWg9zGlMI22uybFOz6Qo7wLP4hTjHF2yjlk8lrFrwN+msblGHRhu63LMMt2jSxYzptnrZrqHFmwB93y/btFt3Llu5sfNmvlrI0NT4xqtacTp6xzXdxpsw44FW2fLuBEmYePDDvOkvtczpBvVWjW+XqvG5Oof0TYMz3bah3TTi5N6h+u6tqPFFpjT9Y8ZSX6tY50arOvkdoV6cY7W27C7GcRtYGqpdXfPW+faFz3OUaY1MD59p2HWfN3U4G83NPZrNW2zuo6ZScdYX31PRye+RWi1uRpnDYN9XbbxUcNi88Kie7aB6xwanTQMahcXAlMmDdve2dU41OIZ9jq817oHawa5YZP3DjvqmhkzjGrtHX5PU5N9aGZwtneo3WEy2mcbhgJ3rnVyTZzZtzDoa3U7uGtj7RN3Jvz+Tq6LdYzptMPTE9Bd9Y2Dg2bOPONyuIedjQFfs35xZDzQd23+uqOhYZJr8+oCVp9FNz+2MOVbMLoHxqY8jabJkTmmecZht3DGrtbm2YnWlsFh++yEtqah7ZrFPHDdPDVrW3Q09fosC3cW6w29Jh0z16NhhxtnzK2ztvrxkQHjtW5D/1CvocU3Xm+bG58K9OqbnV2zXp2zYaG1fV7n0l7rdw/0e9yjXs/UcHNj31KNqX76zC2CLOD+LxwipCPmrVyr3zdTKwxcKrTjaGuDUWXrZCu4Bjw4xCAk4ORgdNRK8ubp5madtbm+RaNv1DLWluYmjW5yqqXJqtFpGcamrWfeVfL50QGRDHNeGC4ZGGp9dhhlcYw/DEM/B6nCwA/ZmIZRHYZ0PCcFHycOt80KI2epzWEHlgkyWHNLYDJ4rg0BO/AHpyYnrB47jOF3JqY44GNAFHkmlUZDQIYDErPBo8vL56DPHLu0JTmdtCGNO6442/tpJRXbkL6luinFgzSWpaAzSxgqKP2a5G3Za9L7+bg9zd3Bmvx9QdmQ1mp4GUjls+atDj/rRQ2Sju5SbeU+47B7ffgC5pXAadFmVRQWUvsMKab3Sm2C7z9C1n56hsItrNAFVvh9//DD0ofsB6Xky37AhmoN8TCyt72VOwL1VtMKTwbflqpdOGemZhieg1snrB6PAxsWTwFbrFlYWKjBR3WNn3OwLqxOZku9WDM1WZM4p1aImGscaOvp76jtH+7gs1vheeXxbcnO1Z3jvoYJlkxzVs9MEgB5S3W9prOtxsT6arpNPYJquvK/RnXUlb+9Gg039xgxfOsQuJJSBS2QIZrRE6pGK3ly9z98X8IrBjm7mwO9aSvLf1l/wb6Va2E5d80Q9FNm60CqhGt+UCJ9S7y8a2DAsFVCkuuMdowaVFm2Kohf9NXZmlaX1bEEvd5bM2yd9vIqUiaoSFQ0AkXXa4bt0yC1xwsRoPOBIgRtxQYKSXVFn701diYwAn388qzdcn7JZGqbnlxov+QBDyM09yXEW2v1uksu22XtpSnbZc2lSSQ28GZ0LUxjE6NvYm1WfXNTPd5O1obJpnoNPPSnGnVbxaR4BqL21HRxbr+HlzdodZqtIlKI7uHhwZoOF9y/oGD020EP5uXDqGbRu0mulm8VEBHt5Oaq6RncKhWaBooO3ajd4ff6WC5QRgpqS9SvoK4UxPpXP2jfvpnAqRgiPb1L1OHAUkcGmU5U6PHgWj5nhrWCduTlC+HudC/A7cvYOYSGgw4WVWjgfuK8VApwBFdzcN3kp1eA9MEM7U28Uw8uS2AOSYnmwMLBGxIm5dCXUepNiYS6f4iRwT0s5wpwqkVuZHzTxyTczlLuigTP4rCL95q3lM+gxrXo4a4ETu14E8fY/hbvYczq38EX7uOqG/D7sHitdW3q6z3v2H7P+P6J97v+9Fz45DNCkPhH7me+MEW1e0IO1yPZJceEcUgmMXOSOm4OTZl38vKWJD/QQGdGu5GZ6kDfNpi3n+MCWWYI3ZY893LV5cDhOBwBBNUN9MEI7p0wkkOruCmI/HMc+CAm94dY3xUxbnwLoK59YKDP3hFj3ypKfXUBFGTU3xHFRs4I2CrNj77vRd8g+W4fvEX/HMdpAcpQnpQXoxbCUXD1aV7mXfKCku9j3H6YuCzAyMHie4puD/cO1ti7wrQG+vcMhygN8rq88JZYjt9lx4GRGyU8BMPABYgdOinkj5w6kGMW2oWX4zkowmko9dwSYYO0nF5e7nF7fVwxdqNsnKs01vPKycZ6YawlOAc81Es4sS0bX84HX4KmwL+r4JqQ4AEF3L9H8p+RfBPj5LKLOALjA5nDZRDuz7G/HiPoCCg1Hu6MSco83gW4r6LTktgxLkWxyo77yKcmJ+eRcoR65/mc6AQVag3HYD5bmJliqMOG1MYhtZK4HqAwz4ORFpH5vHTKy0sdcHkWuC+SEka7L8dipgqiB59NwBMHRHJT5B67w8ttc3NzfBZ2kUk+O9rTj1GicxsyfgQACJY/UJJ+O76OEJDKXOEFgVsS5dkfqwrv9z5WHXmkOhI6OveR885HnP+j+aUwF4hwgZDj+fDR58OqYEQVDKmCP8fz4loRSviCpBtPKXlBYsLDTND4CRqDQtigdFMwNhLC46iO9WOub5a/d+wDyQe6cPWVSPWV0DEX/L5X/t1jocFrIfNwuHUk0joi+H50/Xbk+lRoeiY0Oxe+7ohcdwj+KwMblWe/Xvt+yfvt4crmSGVz6LgLfn8+/2cvPJwMXTOHnx2OPDsseH40disyxoampkMzc+ExR2TMIfiHVEc2SsvfmH/9hbWZ9xXhAy2RAy3h0ouR0osrhu0Dyo+87lozv3MyXF4XKa8LlTbAT/B2hk4ahV+43BQpN610bagPv25a078jD6trIuqalY6NsorXb68ZIHZZXaSsbqVzo/TQ65ehsipvSMUUKlN9E+sSKGYGmEInBoVfuPRapPRa3LdF+CUyTnznhV+4dCFSurBi+LHgOyr8wqVjkdKxFcN66elveL/Z+N6VDyo/GAqfvxo5fzV8pjVypjVc2vrhmXBpz19U/cXUf3KFbllDk1Nh03TENB3unYn0zoRLZ0L2O+FSoa8EIZ8LwsGBndLoETnkbJwFCTkcB42f4BsrY+hCA4s3hozXpcEsdASzIDfFZW8e/vLhB+2vHX/9+FpxpLhqpW1TKss/uF526E3Lly1rstcmXp9YuxYpO7MqXZXiOSEYdgAd4PzFL9bLD21SbZL8oz8hdFUKgSRizjvSf6n4I8W7ue/lhsv0kTL947JLj8oufdD1YVu4rCtS1vW4bOBR2UBocDQ0Nv54bOLR2ER4zBoZs4bLJiNlk4/LZh+VzYbm7oQ4X7jMHynzPy5bflS2DPl/MVbsXixTeR8WECjcGeVmvDGAQvBw7NDECQy5IWUxCI2foEGOBrohnJRYPkMkzECBflx2NFJ2Klx2Bsq7SR0urnunaVN66Ejdg85vtH9T/l7uu6r3VOGTDZGTDZsUeK9TipXTmzKw/ZDK+6L5DfXrh1878vqRcP6xSP6xzSzw38ymJNl35zdz0K6gJKVvtL8tfyv3K6q3VGH1qYj61KYSQ3IpyeG39W/73gp8JfhWMFxxIVJxYTMPQ1QQJ6TWbuajo4CSqENl5zcL0VFESZSh3CObxegooSQFocLqzVJ0qMGx8uJmGdrLKUnJavPmAbQfpCSKldLNQ2g/TEnyoKkr0H6EkhSGip7dPIqOY5Sk4kH75nG00xj58uYJtFdSJb1FG8XqN4Zft7x28/Wb4eLKSHHl+rET67nF6wcq1nPL14+cWz9weT2vZlOPEagYWTVsyqAqSX0S8hMkP6OS/DIR6F4ZwxqpqtN/ePj3D0fnG2M3Ho9ZH0HHGbNFxmzgE77ARoCemIqcmFot2JSqKy48eOYd+SYFlnWqIFSk35SB9YdU+QPVZhbYsJWUK6c2c9AOrZQTUhzZVKIDGqbwDdkbnWREkYXVFyLqC+GimkhRzWYehqu2D8/HcGixI2+bv1H+9WPvKz44Gz7RHjnRHj5qiBw1bBZieBE2w9hmMdqhDfNXbJulaIcmPPygcbMM7dCEZauuzQNohyY89uCFzUNohyYsXe3arEA7NGFJqHR28yg6oAnVq6Obx9FOC0wn0F5JlR5aP3B0/dCljZKyN2wPasPl1ZHy6nDJuUjJuc1qZKFiZDVn8xxVduTN/i/3h050P2RCN20hf2C1P6x+PqJ+Hu6osla8oYDCHVTWjncQ0FXJeim91hoqPRUuPbVecex3m7/aHNU0raHu8UinBazhqhsRoBU3IhU3Vg0fMbMRxveRfyHix3PAWqXtKHFeYkCR88JBqaxwUCoa/4BGPyaNBgkzCWEmIWxUCEs+OPWWwHlb4LwtcE4JnFPIMi2dRWNO6hI43QKnW+BcEDgXkGVR+jwaQemLAudV2c8EI3TTCv69stv4SuegcC5Y1BU1rstupnu2yrpkG2oYRKmK69K37wimQEO2KbETD/+SdknFXqAb9Er7pClcQ8KxsXEvbKFx0kLj6AP0x+pDD6oeTK6pw+rTEfXpkPr0hvrAm71f7n3gfW3g9YHVgQ31wdChhvdtYfXFiPriY/XVR+qrH5Z+OPKdQw913znykAm3DoXV5ojaHFKbPxq+HhqfDy0EwsPPR4axb4xI2rDG0ID02qWdaHRJSXu1gwEuo3RAcA2ga1B4drWDAa5R6U3BdRNdt6RWwUWMEckklgSNTcFYVx9a7VgvO/OO9p2x9y6+b4cHaqgMfxtlh0MVXe+bgcDvA04wv9cqmOGy7khZd6ise6PsYOJJtzqxUXYodFj3vj5c1hQpa3pcdvlR2eUPbB+e+rb9ofTbjof14SsD4bLBSNlgqGwQLH+jPrKhKlo9ca9rxYDfX2wUHogUVkYKdZswppxNEMTp9r/S/6D0AbPWFladiajOhES/TRnwIF72GuiQn+ktv1VF/eBQRW8D9YN6Cdob5L2XZD9oac8Hx3/Obj947VxW+JgKHOFz8mu1ynCtDO1aCdp1fXXg2Kg6f7tE9tfFEqCZ0bbD+2jbfbTtPto2xrmPtqX20bb/CGjbN/fRtvto23207T7aluTmnzraFumdj4e0tUt2xNlyBGfrfc/3sXC2/ijOdpyZ36afLBCc7eIvCWe79EvC2QaY5/c0sgaZ5T3xvcC8mIazvetrTnCADjofR9xeEsV8KQVV+xmC/fytKPbzSlLYy9sgblsTXHtA3J7IVIIMGNEOUS4/y3xujxjRz4swoisZEbdiuff2LHc7xG3GNAji9gvQL++Ldhu/mIK4FbfCl0itv5qp1jMgbjsT4R+rNlc/VqkzlhTRtnB9ZY+I2zjOdjaOr40jbk9nzsP2iFufKcEHUvKWj6H/8rEXjglnUaJtQRLH5b62Ay5XtxdcLheBhAgkl/uISoPkcn9JRSG53GMk61QUksv9FyQ8kr9CgieKcxtI/hrJ/4bkx0j+DyQIguD+Dgn+gfC7p/kcxLm63LinZmfcgTzjwOgA3do51NPeGlCNdA6YOmoGW/uAiZdb3K5pXt5rDQR4mbl9gJf12t28YtTNWKcQQ5st/JEVL28zm/p5uXHY1M/hWWrcf0eyheT/BcIrQdic2+llHYHCHnhCeK0+esDNsYzbDTIW7bg1Lxvm7LzS7LRyvimOdQVU7TN2lzX6H3F89ojLjru1JO9oyTZbfcQ0uMFw8zlD1jm/D09l7+npdUIuswc4q2ua5XNGWc4ecLsC8tbh08MBRexvCUECOSOXQ+Azn4tyoUx2m5WXdnRw/xY9s/BflVnu/8Ny4KEUnASJHEmWJArS5bLRloNEASTwwzSErrapgSB0tS219boYQrcJ/4FVo2va/oy0Fl0mhC7BQwsI3RaNXtPUpNM27XZGmn5PZ6TpG7Y9I034LzExPpdTYoFzkeQhUSHJR0KwDYVIipDgZjRXgqQUiRpJGZJyJAeQHERyCMlhJBVIjiA5iuQYkuNIaCQnkFQiqUJyEskpJKeRnEGCSFQO/ziMq0ZyDkkcf8adR+cFJDVIapHUIdEguShJAX48JUCLe0YShWdxl8GWhMjiWrF/pEOx2jNBsc5L8dAsFEbON25HmwFJB5JOJF1I8PhCrgfJ18iwgbY+0jeRGJGYkAwgGURyDckQEjOSYSQjSEaRjCG5jmQcyQ0kN5HcInlBYkUygWQSCVZXoEr8JwzboXA4BvlnkPwyATbcbLwN5iQpRzc4MbPpQJr2DECaq9gCrngLuNHmQZIBCcPdwYA54keKB+TniKfYCRCz+btf/uo2kBgOD4Xh/JjZzNgXXRz7wn0eCQG+xFl7W80J3IvAOo8CF5AsIllCEkDyPCaSAmrRxUAtZ7kg8iwjeQHJi0jicBbuLulBaIuDWbiXSF9C22dIImjDszEIiIV7GW2fRfI5kg9SArStxEeLe0heIRWAoV9A230kqCnsAa/CfRH5CFDl35GHT0cMvlJ9XDjR49X4QLWK5DUkX0by20gQxcG9geR3kLyJ5AGSryD5KrnXkLyF5G0k/wzJ7yJZI1lEglgU7vfRhjgU7p8jQfAJ93Uk35Dg2STQTpPcH6JVwnqPU7uBT6J9GAuVAX3S/jPs7I1R9MlNibJ4H33ym4E+wYCxbDFFpuvZPyP06cAoGxnBKD/8NQCjBAgYJZAFuflUwChXEIty5TceirKxD0X5JwhFKY5BUYoTUJTiOBSlWARFKRZDUYp3gaIU7wJFKd4FilIsgqIUi6AoxSIoSrEIilIsgqIUC1AURJxUFAtQFEScHC0WkCjFq6c3jxcLSJTy1fnNE8UEiSIpfqMqDYJShWFYNas5myfj6JPOh4aQxRryLiL6ZCmiXnqsfuGR+oWfEPTJzwj9OLgTmz1i837km4/4XoCb86q0DW9Av4RAWdD4CWqVBIWCxj+g0Yc3LhokzCiEGYWwESEsCmAgQAuLgGNgJLcEzlsCJytwssgyJbWjMSt1CpwugdMlcM4LnPPIsiANoPG89AWB80WB80Vp6OZz4N8juyWDZ/WAbFgWdSWMMdmNdM+rss4Y7sQSxZ2QUQpoiJ0ROwl2o0cq9oKU+oWBXsw1LL2e5IUtdIO0EHnIAf24uBPzdw48LPnO4YeG7xwPq69F1NdC6msfDcFw7Q35FsJDi5GhxcdDLzwaElqyHVMzQJZ/gi6S814BfHI1Bj4ZElxDwp8KjguuaKPdFlzEMEvIUaFobArG9nATPMSt8/12IPD7YFIwv6cVzLC6K6LuCqm7MhVY+35VWN0YUTc+Vj/zSP3MB+YPy749/iH37ZsPT4Yvm8LqgYh6IKQeAMunBTfZKDyIbMUJAhEEkUQsjncy8EVEyhglIFJOiRApp8SIlFNiRMopESLlVAKRogXHxqnzt8/I/rpUibQyC2hmXErtPi5lH5eyj0uJce7jUqh9XMo+LmUfl5Lg3cel7ONS9nEp+7gUIn8fl0Lt41ISUn5puBSx3M/vCZfyCvTLL4g26e7vgEv5Iqn1L/2KcCmvfnq1+Y+JS4kjTlZ3QJzo/9EQJ9XZ3A/R/jdIfoTkb5H870ACcn1tU8O2aBTuXdwNeyqAxUYawKK+vp4ALPQttfqmegFgUd9Yr2mp1zTotgVY6BoaEwCLFl0MYEHOlhMAFjqtRt9Yr29q2O0ItBbv3B4AFpqGlu2OQEOARc18E/4N3T664tNFV7RlQlfc+81CV5yJoSsma3Y+5+TXF2HRlgFh8c8+IcLCjzCAbRAWva3mPQIs4seFJCMs9AmEBcFO7ICwEFj3Cq7Qx8AVZ37DwRX/Fkf+Y79OiAruIWkp7JJ7PcoDC5EBTNFmhr7prYqCKcb3j/LYB1P8WoEpFgiYYuFTO9ljH0yxD6bYB1P8EwJT9IYGh0O32dBCENEUyxH18j+Qkzv+nlDcsSdHbQDdx1R8EkzFeBRTQTINNMRMi51knOuWir0gpT4BniDmMkvHkrywhSykhcgwCHRvmIrG971h9aWI+tJjdesjdeuHVR+y36l+2PadCw994TZzWD0cUQ+H1MMfjYyHLOQsj5HnIyN4lseocJbH6C/hLI9R4SyPUeEsj9Edz/L4TQJXpJ3l8akgJ9Syvy6VAM2MmfjXBfuYiX3MRIJ7HzORkXMfM5FeJ/uYid3j7RUzcWMfM7GPmdjHTOxjJkhu9jET/7iYieF9zMSOfBkxE+Q/8+Yz/mfeSyn/mZeMlEhGUWyHlPjl/2fep4mUEMv95SElru6ClKhNyscXP1Xswg24bu0Ru1AZt8VH/Th24SSV4bMn7MKXdsAu1P+anpbxMfAJf5WOT2huFP6irbFWp9NED4BobNHr61taUg+A0NY2xA6AqK+P4xMQqxDFJ5C/thPwCc0NLTp9Q2OTZld8gm8vB0BoyH+9iQ6AaEj7i7Z9dMKnjE4wZEIn/Pg3C51wKoFO+M08/cGQAZuw9QmxCdz/gmS3Yxzq9w4yqM8AMggcSMYuGOtj2IJTv1bYgt9D57awggSi4EMkX5I8xfY9xsiwfW/4l7h9/38r49v31fvb9/vb978+2/d+sn3v39++39++39++39++T9++3/8njl/JP3H8+p+IsP0/cfhDoL4MByLDAfJPHK3CP3G0Ynpt0ugQTdAWbcI/h/RLTYLLhK4B6bDgGib/ryG9IbhIdm9KnxNczwn/xGEV/onDKvwTh3X73fufZ1Nlh0KH8F811E0RddNj9eVH6rR/1VAPRtSDIfUgWHbeia9OkPX84ldvvnITqtC3NhTOPxvJPxsS/XAnvlq0E3+zOrETj/b4Tjw4Ejvx4IjvxKM9uhPf2wCO/1p9/tZB2cYBCdCkqQqutJKd+C9nCZPCZYlPFJ626y1LhDHp61lZiVBfjohTutPKIkw+pYxsjqwGcUVJKchTU3BdA96sOXkG3rS3bVyXktZ1U/JgoG6dX5YFJWuiPG+T+5ygjFHg/AH3wd+W7VQWmLZd8IlWLWfjcpj0NUVR7n1FCftOfEyeeN06KNqnTtllzIR2EMtR7RianxqKu+eOPGfeslxCSamgfDa+/5iyip0VzNpm1bYobc9enGJxMDt1F2WX/B4VhZa8V5oc3kAt54hrx0CtSm6dWlYoqaBiTbTTIJKhTpZAFkaUy7nB3G34y1LKk9wyeSm7R+VC//a27Mh1IMp1ekeug1Gu0h25DkXvKOjjyyrX20iZwz46EWOe4o4Fc9aKM5UuKNoVCyqDuUFV8o4G3F0+puIppMVzuo00I3PkKaTFd8q2kXaaOZoi7egO0uJ7OZmlrUruH68i679gOyms/iqpp9v589UkUvTViuyahD1VFq42Vx8z+YfAlfxWSMpfy6a+DdLtXqCdVtcS7Yn+3biXZtz0kttPL1hdPtrnpq0M42/bk9iE1EG/j+63O+0+0X/b0jRZO/LjOmru0wpzEGGTrG+BZV20FvOl1zzBpvVbnkoe2mP/rB6Vap5x+x0MbXL76DaW7uJYq4/l6OEZqwvS8Ld8jKLHEyCL8P58IkJY+xcq4jkKV+Po4YHh1n66x2CmOweG6Pb+AVMHTV8U/QnwKS/NrSFvbcJzxMvSrXbO47C6WNroZpBwLE13ujna7GFZhh4ZJFsD1RJewUBZfHYnG1Cc6r54ynjxlNmvTxQIpLU73C7W7pqmzT4r56OHgTfz/xE/wXUp7gEScuwqNuMTHHWFXYlZJINI8B9iybsl5LROskxVfYiUmCyG8TI8ePqP0JZFTqkWlsPIshkR9w0qtlx3F8kjCcZxuRd4hdfHTWFheIXZbnXi/9cKy3XfQWHZXv8ktGam5Ll/QcUW//A9nup84cUdfLOGl3odcHEkGe4x+qhsfo7Dv80lSSkxGWhLB8PLAt5JXuaP/eev1BvgZZ6FRS82b4b1uTC2W6FofQ7usIU8KKLXIMPFufXi0pW2DVXxva77XStdYAmVcGGVN6LyhlRenO6OhCpc4TJ3pMwdLvZEij0rbeuFxattryysLGwUlYXK58JFjkiRI0R+IG118ssHVg+QoBdBeS0my3jFRCuO0x8fPr4m/Ur1W6haFqOmjHS1bV1d/mbPl3veZoHrVLs05HCF3J6wwyM4xRQEHyezpeOGJCj1pohuqAru96xOx9cDoWxvnLzXd79vpY8U8/L3ZB8avtv1HdV3VeGS/rDKGFEZQyojhEH8UrIykk9WRoBuEkqidYRVnRFVZ0jVua6qDiX/1kuOrZ59/cJrta/XrrTjXPCZrz7zTm64Qh+p0K/0k+iDoaHbYdVERDURUk1E05oiaZElGaCbhG4UH1qbDBVXh4urI8VQT8X5x98ZX684/lbTJlVUfPwnSFbbN6WF6uPrVaf/sOX3W94x/96Vr195bWnV+8CwfoT+3d6v9q55vzLw1sAqt3H46IPJr5x568zata9eeHDhm1XvTL575r0z71/7owvvXPjzqg8mv33mz858eO1/vvDBhb+oejj5/TP/6UxoZPQHFx5eWK88+UD/QP/DqlMP2tePn/1mV+i4Hn7rdPVjWvOI1ryv/tMjH3g/NDysCtOmCG0Kkd/6iXPfnA6daIDfr5rzv/9ivfTYg5NfOYmLJyegkjZlUHWk/gj5CZKfUUl+mQhZe0n3/vlJKr/0Df0b3nsD9wdWyNd7Hm6x753O662UfU9nONSbL/9BnhQcP8iX9pbk/KAwG+2V8t7TOT+olgA1VefyiokJl9XJTkzwuRMTTjfjd6BdNTFxx291CCHcf8Tb97vxsezfxUeUD2P3tbDJQrZHyL3+H2IENxe8+Lbe3fh3UyrJKoUbLUbkhVlVm1ScVN6WZJ3dpET0quyWJAu6p4i+ILWQcBFdRK9q4ojRRenZrCObVDoRcor5s4nVmfh87nZsPkeJ53MJpPIuszfRzvpOfKkzO0kSliZt9pgnipkyj4J5504xf5llSJtl7pgT0ewmqTxZO89xk1JMPxlCNMfIMFNtX5YxOWsKKsOHUbycFJtRpsbeESEkD1JrotKKcpFWK/cNPhHqicl9Ly9tzpX1qbfTARFfYpcUtPYdazs7qbZVweyMKBkxT35QsitPwdP0kyC22/MwC5UEcwjaVzFNBXME+2sSphCuIriK4SqBqxQuNVxlcJXDdQCug3AdivIchqsCriNwHYXrGFzH4aLhOgFXJVxVcJ2E6xRcp+E6A9dZuKrhOgfXebguwFUDVy1cdXBp4NLCpYNLD1c9XA2vSZaV283jfUdEraCAGVN26nzpfvCpZ0c73xvi0MYdQ3eO25QWKr5/m9NCRYjdtDc4cG7WYhKU/qN0x/VW42B/B91qGqfbB0ZMw0PjtLnHCHZDR6CMbu8eMHfEPeiL9OXLVwK18Vj9PcaeYfpGg0ajuUXf0GoEsyFqtpDPrUAR3WMaHBmm6f4OZL9IB2prnupDpmqZcQo4xYzjFCqTlwATt7FP9ArPbHxxJrnaotiFKqwg7vvgUS0XNuZxJx4Ueh8HExM+m7FP233eail3RRJFHaQjG8raMiEZUNH24gz67+B7lwqVdcDv/TtvTL3u/Ebn143hcl2kXCf4in/kcfkEV+OeENAPTnoCpdgyPe0wQWslrWbGWq2IeWJ7RRssNtMLtMRsw90d9ODQQHuH2Uz3mOmhEZOpx9QFTURC2lrb+7qGQKSBHuy30GOtPcMB5RTHsvSUnWMDyk60doKVV6AvevKqmE2r1elELp2+PpAbc12tCuRYXQtW7moVn41BDY28QjCbmnmV1zo5aeemrU6s5DzOOmNlog6F3eGeZ5fcfj/2eSHG1aof/uGf+JVRN9irrvJZM24v6+JzwPDCNIfPjsZXOu3OmHXWOmNn5mAuzcsJzZu1JxLKnbVy1jgnBkyCKIJuIkk3NtTrdVqSmB8faCQTp06f43NjxWjR8Mq4nc/1+Zdi8nInYXLpsDKsd4ZX+ayueTs3A9NyyEK24Ir5xvitk3GOLK91zj7J56ERyyv4+WbsOGclQcQQggJHegwW2tw62mHANh3oQxgK9A4BjxI4Jm7+7lYz3dbRYYK+grfzcIchoB4cwpAO03DHED08QPoDXV0kmhETDAmZFv9zJDh35j7Ce+EvJTE4Cs6h+Vz8zyYrM+h2OwRYC5lF8zhZzebIHJTP6jAOtaIeLPd7WQ7axM2wfBZZB+HlLuckB1Ntp4fPauWWoB6kPgcvn/Zzfu6HmNKPULnNpcSzXeEW/NMYacAbrkNOprfKvLuGDXn2yz0r02F5eUReHpKXb8iVXzz5Ut/LfXf7wBrKrQ7Lz0Xk50Lyc+B8qevlrrtdG3lFoeKz4bzqSF41Coh57yLpYlh+KSK/FJJfSkRRFb6RFSo/Gy6qjhRVh1XnIqpzdzsgeOX0S8aXjXeNMFVeZV9Tva7apKRZhwhZka8XFL06/cq0MBL8eceHJ77d/WfdYA2XdUSAFnRECjpWZOsK1at5r+SttocVByOKgyHy21CWrklDyqqwsiqiBPU+L+vCmn9DkXtfuXomrDgcURwOKQ5vKPK/yNzLu5+3kreRX/RG6erwa4deP3Tv9v3bK1IICxVUrbWFC06HFWciijMhxRniV/uOL1ygDyvqI4r6kKKe+PWHFcaIwhhSGMF5L+d+zkrOuvrgJiVTXiBkxbBeUr7qe616BSarVLE/Z1W9yryGe39gf3BJMNeeF8z3LwrmBy7BfHhbMEM3Z6IWOxe1eKNRNlEP75LGHd3S0YRjTMokHKzUnXB4hBeSBcfz0m5Z3NEjvIQsOEaE7UvBcUs2lXBMy9wJh0f2fMIRlHXJE9mRmxKOAfnNhOOW3J5wzMr9Cce8/GpW3NGaZUo4BrLGEw5L1lTCMZ3FJRzerBcTjqvZ/dlxhzH7RsJxM5tJONhsb8Lhy76ak8hBTnfC0ZMzmnCM5dxOOCZyphKO6Rxf1LHSvq4qxnd43y5fk621vyMNq85HVOdD5LeZg92kGHoo6aaE/ATJz6gkv0yETNDTvX9+kMrKjd9aeE+eDcurI/LqkLxafNNhyLmw/HxEfj4kP0+cdFh+IiI/EZKfiN+8+PXiRsB3mw3yHqXs+0p5T37O94skQNP0EjKJXaVwErvdpCKIL5CmTJZmEy8FSMSbeKng+2XozEHpmvil5PgnWdmLbqNIEY3JyEHtyzIFDDGMqA+efzMO+xxL4KG49uCq88FYXTfN+ibi0FHPjOdZ35KHvWybYW1zDvs8e9rOXOblaINxWTAYFh5G1VkCPPE+kntUDMuIuMVqGRmx+axulnO7yKFBSZhcPgflTNjmuMOQYwuO2qjp3KU2ckvuXwgdsIVuW5EesIVzmQj+7DByKlUrI/cO3z9817Cek7+qRvAWgo4e5RwN5RxdLyxfWfghEqI+2UQbclRerI2eyxFe4Q5KDNSq7NYzy7LdtcfUSai4pWbjfBm2FjNu1qZOL2fjE0qYCGZ+rUiatHWWMm1IeU1B9GKHKM2U5YvtXqX+FaWT9StKJ/vTTofJYXKCFG6wM8q3lMs5dvJi729L8GVxoAVMIdAiBl9pK2FKgaoZfL2vnDkA9CBzCOhhpgLoEeYo0GPMcaA0cwJoJVMF9CRzCuhp5gzQs0w10HPMeeEVSaaKqcVXHBntW9nfkCwroH/lZcyzDibuivf0yS+EiHoZTJYTG+KZp80pL0rt4QXS5VymPpg7T3HrTMM2W9CNL1NPnXLR7jy7LBnlBfPwFczPilDryyrxC5VMS1BFXt65SPDtMmK/lHF5RRzrmWAe4byckfNUgjNtSe6MSMoV5tmUfpjxtcqgKil3VzOmeS7Bn/kVvmAaLEFCuf4N00ra7VvbtlvbP1q7tTOGHdqtI0iltVtnxpoR13jXHmuc2kONi7bGn6LGpauy+1fEW+mMjLwMdtCnS/glXnTMnD+mWyzB1ySyi/rB7seKTEmgHJnTFS2diSRS6UtLVfHXzaIvm/WYAhUxncM5afXabUkvpgQO4jbH5UqHl6mk560OP9jP1p57trqS7FYHjgjBs9aAm/X6UlgCh4RQ54TPmxp0ICrXnioW30IKZPe7p+keV7WSl0HKfE5UPi9HUbzUYYfZO7c04fI7J2FiWuIHrcXmnnbZAywz4ePsrJe8+cTLEacAM1Z8r4ZX4js2bs7uWwqUZigp14gxZF0dwxzqCQFaeB2njmHn7Ta2BiKwTNTL6l1y2er4bC9oXU5QsEj98dlWG/59ZuDzPnbRVzfjczouWD0eh91mxb/UrFtEn/OLqb5Ox6U7lzW1LRfsTus0W2edt09FrQvspCfm63FNXzhXd46wNicJ8NqnXSxTwy7aZnB//NL85Uk9YWsKFAoZqnFAgB/EBA6zrpqutgtAR8zRVFmXIDOQb7NCaWpsbpePczsCSqd1sQbiXNbwMsbDBbK0tc1NDXwOx06xHMsF7u3QZ4RaIrqpC6riMmE9pW89peuEnzOJFzzQ6rRyc16wnwb5Xs52mWE90KJWH8ucXvB5QaXlGG5CM3a9XedhphbuMDOW1u4p0+kJ8A5UeFlbjW2mxkPy5oUiONxcTbRt5AxI5t7CBj1TaXL7JlrpNs7qYiqhoiqbKy/Qle0znNtp9zuJj1anqYwL9FtrpvwOR808SIWqrsH3zgLN6VLIO4uaTLLAv1HT0lKr1TZWBooSYp3kj7UD0me1gUKxL8M6ArmVZmNNq0bf1FkZKEkEehxW35SbcwaUla0uhnPbmcrA4fTgWGYDikqtnmQrUIBcU6wPGBm8hxSM2+Z3si6wuaC7TUMtB/K8cDfWwM0BDUfeDQy4je6A3eGw1jXUauiz/XaXf/ESHU2Z1mou0X3VdCv0Q3aMneyz++oa9E21+kb6bF/3sLH/Ao0zF7oL5iTuaprUClsn1Ad8o39VTputU1bOHo3JfZXC87HFucX6ELu9dl+SGxelAof8nmnOyrA1dheE+Dm2hmP///auPSiOI7337Myws7sDLPtieWoQoCfCPIWQDTYgIYEeliUkS5YQXtgF1jwWzS56YLluzqXUrVLcZe3gCFfiCpWqVOH8keBcnFIqlyr7zo7tu1QyQ8bFZKqwSeqcyv23qrpUufJX+uuZXXYBYUlOLnUVMx+/6Z6e7unp6df39ff1XpvG7xmdscMNUIlxlX4H3unpb6y0D2/tey3GbqrDREA2NABpb22fRywhwfrXtITMXbeEDJJR8LaFLNVYZvMexRay2BDGbWX/eI82nyQhuTxg0HtFS+6l8/PRhca3byxMv/1aOsCQU98DgIFhpgAEzo0NE5eJYfHzJ/qFGVq4LcxYSy7XPd3aMjEN8yL75X+TfoQp+cc//LN+CGhsnBDA1K7nqNBGVH8amyZmHCDcM6PN2GFHYUOsaRjsga2ebicM6lQkPBn7PyywBXy3WGcxV+N/BUvvv5pfL4x6szC6zvQLIjAZMw7TT2SzNSmbbHJXf4Yl9u1UdFyMhw+AIlbu3rKM1QlmGlfCDPPANBOu41qFx5FQQBwaJQy5zo6IkekpYiyoW4dw5cSDmc4B0x8MD+EBcCx0K5phVEikvUTQS0wEiQkj0V0ielJkI2Ji0bhu5WgoS1FEsyktqBXdUChQHjo9JUbI7sG6FdYGBoYHdQ43hIFgIBbQc0dDuK2JA2TVYBAPxBHdAYFmRsUfkRSGwsGH6Tk5LCaEQIywnwh/k3wHxeZqLm8SPW0regAQ71x1+ecO/CmjuKpVV3W8a9VXrvp2Kb49qm9P/JjmK7s39uaYvPNZxfecCnQ0fuwrp2vOJhc3vT90f/d74381rji7VGfXirNn2dnzaYXiPKk6T676/HNhWWj/mP7A0CjynVJ9p1Z855Z95+S+84rvguq7sOr2zrXKZYf+rvL+yN/U/KRGcR9T3cdW3KeW3ac+DSjuM6r7zGqBe65ILll/WEGXWtC1UtCzXAAPKzipFpzUikq1iirNU6i5vZqnNOm2+cuTCEP8eNJTWGaZvyzvezaJsEtj+HgoSWPXGmOX+doki53JHMTmxkeSVnBz2J1EKP+iJWkDvx2xPrmwMekAD49YT+JyMhfceSBXa0nmg9uJ2DwcyXnZkiwAvwuxOxcOJt3g9iDWKRccTnrB48MBcmV/shA8fsQWzjPJInAX48ckbidLwF2K2KL5/ckycJcjtmJhX3IHuAXEehOvJCvAvRMVVmi+Ss1XjN88aUHuIxbNV5I8AGEoBfFTyQbkKrpX+mapXH5ZDoRl8XuJ0gcIuYgSmondlnin5t/xR/kr/rplf53ib1D9DSv+lmV/i+JvVf2t8RNr+YXzT8v5uzBpXv+9i29eNLq6+yM/iay0X1huv6C0X1TbL660X11uv6q0v6y2v4yDlfKAWm7a7yUYnNf5xvnofMvcRIIm+nA1i+cUX92SV/EdXBIVX+v9GsXXrTiPqc5jsvMYueXIB32Kr0c+eVXxXVWcA6pzQHYO4JA3rHPWhHXV6UlcWWhUnLtV5+4V54Fl54HFoaXqd8P3Le+O3z+i1D6nODtUZ4fs7Fh1uu/Z37TPN76RP5efyNec3gSrFZQtlMgFNZh+k6/lSfQvdCnOPapzz4qzdtlZuxhdan731n3Xu7dxnp/aPs//6vSvcnw8cNcaZ1Y5x6x9hfMvc3656OznfRc/v3Tl8/6XlUsB9VJAPjeoFA0q3JDKDclcEFPG7el1D4PAiBN3DDhdJs6A1Qowtq+frjq9B/3jHsvpA3SWghJITYjcsJfdTrb7xAojmdtBZqadjr8tj4yCltvoD6kgDfgO8xr1yM/9n36PLAWlR1BOYTeG2tBDDFE2SO3WpXswlN+2XEfi2cyUN0lbvl0J05kSxIxtFq3bqf5sxSNnvT23bdnYtg3dbJjz6HEd24ZuNlrJUjl6TGWjDPWnYP4mCfr/Zv1zwoZJG1daNtxTsG2oa9tQ97ahno2hQe9rbFZp+DaqfwULDZWvoN/YYYO4i4ibIcpY1ljGdlavpKWxIEu+zRpKWiP0plxtXXNLt8192eOqFYHsJ1aR8aSCh92dJSEqN5SR9Hw8sR8LT47U3zw42DLYPKTbDzUPHppsnRwOhmfcwqXItCicCN0SDgvmbDit0/J42kTwN3M0xaqNhGOj04OEQ+uIhoejAVAMCbccOpjtfWpwPDL4FOjPP3XOuEYYECKjqk2p1pyO3BDCMeEG5muFGxFxTLgRwq7wpBDAp6HI9CQRHc10PXG28R+Ji7mn0yhtxpG2ApH+JMUzrOcoForiEgOGQuiLRMajQldgUhicvrUpWxXpfKW3hKrfmNzZ6OFDdXUpkwzMnouR64FxYuxRL0xEJmOjM13Chlw1bJFI08MSaRaCgVvRmd6NiTRukUjDQxJpIWkYlQTzi898m9Ke8QrnQuOhoZjQiYvs+SkQiYGqVVHqyeu1suRyY/3TuFKWpRWtSHHjv8NCd6cApi2gntOdimlPOcwTfKrDQs8wVHShQwwJRNXqfDQkCkcik7tjQldkIiT0dAIfXDcxDTtt2dMfDH/6fqEbhB5dwJuuP8MIORuYDEYmzLDUxaM3cV09I0ZGxMDETPOTFU9LqhnBhkM3RgOxaGBqijSmaGgy+OzUaGQy1La/taGxqb6lrqGutbFuF0gv22Z8wtFJMGy6BeU3NBoJD4WgoGZGj4eFaFgkFbZG6BFOgwlRX4QUPynrjJp8wRBFCc21Dfg9QiAYE86MhwJgkkQkk8KpW+Tb4PhmuN0unA7gYsRP4uxmbzKTbyfJmx/6sKBbAhM6GwUTJPEvoYFffqLCsQtnp3EbG8F9Bu4SYqPCVEicCEdJlodF/DkCwYnw5F7XlrpVZPH8Okpt+rO+qv7XAG8BvI9M9SvdHp0exA1gKBSN6jwRhAxEpmNT0zGdIxY/ganrBoMOffBejuwepOdcvBULhULkwTo9ER3Rc86Eh4ZGw3rOtDg+cCNgiBbo2Fg0ChOtbD77pMWEvwA++88tZLl+G60oR94PxdmZu7dnbyuOUtVRKh2RjmgH6hf7FvuWqpaqZL5F6s7SospO6q3pd/reeHXu1cSrREWjcqFb2ai2cVxhelSmR2Z6kpZy1r1aUDSH2b+QUjCsAo3FczRHQeKC7CjBtG7p5PK+NTj3yhvjc+OKq1J1Vca7VnnnbG/i2t1Ts6fip7Dnbvdsd7xb453xI19lW/4QS55+hb+q8ldl/irxTip8ROUjMh/ZKnRY4UdUfkTmR7byTin8NZW/JvPXiPecwvepfJ/M9616i+WSBmP/mHj3N1k0PbPUjQGTwrepfJvMt5HLTQrfrPLNMt/8PlhWtZ0Fc6OWc8AMt5CtYjD+J2yhYP7uQ4R+AL4p2OUBTknjRNLqUfhele+V+V7NexrnCPLXqHibVG8TLiq3sZ3FMbLTDlHKOm45RzzpLWnAY+5QQX41wjMBnklLjHhiFvgMPpWvXOhbbFnqvt/13km5qkPhO1W+U+Y7P2766PCngQ/bPmr7oG1TyXnu9s72xslBGDw3MIDcXfusPW4ewOrBStpPn+o40GtHH5Uf3YdPP7d7e3fS4j+D6Or31xulTg+Ni2TJhuyrpTMz4+FBnZ4KT5GGgj3GblykgZHWSfbgIsK5Q9BK/gO8r6aasu4aikyaRn21w9OxaTEUFWHaJdrxzbptIgQLLeGZkO5OCZprQzehN8P9RpRsz6W7TxFTITxidOPRO3hUFCOizgwPjkXFJkipHqAGADZRFeFXLkWwHBVBZVqEFT4RhK+6pfO0Tnd2nsSOM/i/E/+fwP/H8f8p/N+Bu49bA2S5w+gLWNwpTAYypIsM7nVuZkgGPwH4LC03/CcAmcQEAWWD2AKvaIVIIHXMCxji/gGyMBHVLTdvgmbRpGGEqdPTURFfC+oW7ADlUtwvB3RqUKeGdCqo22CBhNhs6tSwTo3o1Kg4DndRr+jUmE6N44cGxqYbdJZI6HUO1loCI5OG1FhnIFDsB6ftXF/XwJmOFzvO6lxfx9mOgea6Zj3P+La15kcQB0ikiUBsVM+Jjk7HwuO6dTQQHYXvT6xCmZgYCupsJHr2fCeuMxNB3dEzMRURY+TziL9DOur1b29svjYH0Es+fIyoyxLl4zAeGUEXK6rbb4QGB8XIDVgM+Bco1/Op7l+no+NT4h+glE6tbTgQjQ3ArFNnjTnd98h643h4QrfEptYNTg1DVvIbbvBjcTobi8QC4ymzVaNA2WjgOn4ZjgQFJ3BNHw6P40wZEl6ydxzZRQ6Wl8V2UjIguNUdw5FxEN9OQTHhsWcsFAyL0QxtYZjoGwawZPT6W4Afo5TNGtHcLU5JcMnwotPi6PQGA7f/4p4xbOXaxbctwE7gEejHuD0naYqiYN8iu2SDQ0OlcjZpyC1nk4YE+UlJQw6JHBo6JP+mKGmxUjs0xi09D4fGdMnZpDEeOUUa0yhvoq81a3ESWagd66AxuVLnnR4576jCdKtMt8x0m5fiEYUpV5lyOUVJFt8POpc5iOK/e/v/r2+fE6MkRmOcEvVNkJtysS7JouW4JdpwPQzWKIvUIV2LV8RfSFCJ+kQAt2q+SOLWOG88ZzY3MapwO1Ruh8QmLQxVrVnd0s07t2XPJcX6kgo0IHk0ipU80liiUqF8KuVboUqXqdL5PoXaqVI7ZUK4IJxJRFHV66BROZJXtuJIVSpVJW+ir+HNcQ9TbZaAXeqL708MKWyxyhavsDuW2R0KW6GyFStszTJbo7C1KlsrMWs5nMRqrFViIMN5mt0X3wNKrVcUe78KNIgnwgwnHYmXJaIKU6IyJStMxTJTsbA7bY6AKZXhvHXQGJt0NL7z+z13eqSMI5XPPHxeI6Lt/vlGo9BWuKplrkrhdqncrhWufpmrV7hGlWuUrFp+gZQHGeQ1mzfuny2VfZcV2xUVKLBiG1+2jSu2SdU2KXVqTheYDlcRiDMa51vhypa5svmgwlWqXKVMCOeArfp6DfeQMSkGuyMyORIND8hNf7I+xXpeBXppxRpatoYU64hqHcEPyIM3ZQsJxC0a5/g9++/aEw1382bz4viApAtx0impPf4YDme8OsHc3T+7P4nyKQ8BqTPJIDaUK7k02ikdvNMmF1wwSKFfVOkXpYKkBTGnWanADMfzTxeZn6YRT0WZPpgfY4Tb3NJBlXYnOvCHoktUuuQxojZmxO/MjJ+TEXBk3qPQ5SpdvvXNkN+XcnGYI1fmWjElKPP8AoZ58MzXAwSMywvgWTA9ixXm2fQvmf4l0y95cbP5QcnrJfHzCuVWKbdMaC3XFT+faL57ZfYKlGo5AekoLlp+Khd/HHthfNfsAdl/yCDF3qraW+OUZm8BIIG4QIrIVD+NuHAcZFc2jHBbcXyXai+er58fUuw7VfvOx4janRG/ITN+bkZA0wKj2KtVe/XWN+NydbwM93sLZVcXpvkK83wNwwJ4Fl7AsEgZlxfBs2R6ljqM833Tf9/0f2D641zKOue4wpWpXJlMaM2ej6sse7dmtiaJSinPAwBcZfEnHsnNqmvXFLpIpYu2vgb3v8hmhHWtV6G1R0zjcZ51CfJmd8jW+vgLGDAlCswz+HEdxABeXAfJZVx6xtn0L5r+RdNPemtS7XD/7FIpl0y5NrXbeoMUukGlG4xG99vXaO28bD2EKX7NOCc6AMCDqxuGF4zLUGCHFkzPYoF5Nv1Lpn/J9G/VaLEjybAwRqTBiXKL4sdnT8rFgwo/pAKNrvDRZT6q8NMqPy3Z1hz++MHZtvkixVGpOiolDmY4nk1z5Z1yNmnokvzbQN9ulr+Ri9ieNNQqZ5OGnpWzSUO2FIuSL5HjUadHGTFtkuWOLb5PQV4VeWXkTV2pUVChigplVLiG8qSsYw2Vy9m0FY9kJLNbQS4VuWTk0hArsXJOm4LaVdQuo/ZkDkPtSs9Dpefx5MQFk8ld60AmJ5kmlel5ZpXCVKtMtZwimFXugmGc43DTR2lwwfSOKZMzKPWc6nUwn7Nu3JV+TqXCVKlMlZwieA6ZuzntVG4SpcFPU42ZE2dMxjSZohrXIZ1svcI0qEyDnCKYajXCVAvtl7ci3P4pIjv7Dr/D7/CJUUNtcjZpCA9QJmmoWM4mDZXJ2bRVV1ciZ9NmAZFBa6heziaNiN4XG2S+VuFrVaBmyYaHWpsd83tWDrPHOVbozXOgX+ewiwBmBC0GpK6xeGaAGTAcLUfjIK6DlziwV8/REH3HvoKcy8gpF1QqqEpFVTKqMhlrD4A7DXDNuVc+NChff1W23saEc5BXLjmSFpqyaUw+7r5OJBwLQZnZn144wQQicgjHHCj0YsCmEV4NMo5ZVo/1JQs+76OoIdifbR0ZC+WEHtgEn5XKT6I0ON2UN4nSsM8CU5E05JRDQBqeo6I5VGkSbY0PCP468/oruTspPonS0EvlUJhdTIPvGAW9ewb2WXbjaRFKw1kK5eRJF+d3ymyZwpapbBnkrGjBvcZYf9D7em/8psL4VcYvM34YN4pIKIEHAL9GWdceCsQ4ebsbovBLSh/meToq0YeV1Z0O+qd2CrDF08Wjn/HVXU30zxopjB8JniPN6KPm6qNl9MelFMa/39F0zIM+8bDHaulPihzH9tKf7AX3p7uaekrQZyVsTzP9meDoqaM/qwP3z/d3UCcOoF8csJyop3/R0kGdbEX/0Go52UavVjH9e9HqXuEqT3/hoADdzFU/+sIvXH2a/uIwhfFLCzNgRV9avQM76C/LKYy/tLiCXvRLryVYRH9V4gu101+1M8MW67+zFMb/Br7aUQk="))))