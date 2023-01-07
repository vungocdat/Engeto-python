#=======================================================================================================================

# # Prvni lektor - Roman Pavelka

# ----------------------------------------------------------------------------------------------------------------------

# # Validator ceskeho rodneho cisla
# mnozina = ["honza", "pavel", "tomas", "honza", "jirka", "tomas", "jana"]
#
# print(mnozina)
# print(set(mnozina))

# ======================================================================================================================

# # Druhy lektor - Radim Jedlicka

# ----------------------------------------------------------------------------------------------------------------------

# # Nakupni kosik

# TODO variables

potraviny = {
    'mleko': [30, 5],   #30 = cena, 5 = pocet
    'maso': [100, 1],
    'banan': [30, 10],
    'jogurt': [10, 5],
    'chleb': [20, 5],
    'jablko': [10, 10],
    'pomeranc': [15, 10],
}

# TODO naformatovat tabulku
nabidka = f"""
+-----------+----------+----------+
| POTRAVINA |   CENA   | MNOZSTVI |
+-----------+----------+----------+
| mleko     |    {potraviny['mleko'][0]},-  |    {potraviny['mleko'][1]}     |
| maso      |   {potraviny['maso'][0]},-  |    {potraviny['maso'][1]}     |
| banan     |    {potraviny['banan'][0]},-  |   {potraviny['banan'][1]}     |
| jogurt    |    {potraviny['jogurt'][0]},-  |    {potraviny['jogurt'][1]}     |
| chleb     |    {potraviny['chleb'][0]},-  |    {potraviny['chleb'][1]}     |
| jablko    |    {potraviny['jablko'][0]},-  |   {potraviny['jablko'][1]}     |
| pomeranc  |    {potraviny['pomeranc'][0]},-  |   {potraviny['pomeranc'][1]}     |
+-----------+----------+----------+
"""
#print(nabidka)

kosik = {}

oddelocac = 40 * '='

# TODO pozdrav a vypsani nabidky
print('Vitejte v nakupnim centru',
      oddelocac,
      nabidka,
      'Zvol si zbozi, pro zaplaceni stiskni "q"',
      sep='\n')

# TODO while cyklus
zbozi = input('Zbozi: ')
while zbozi != 'q':
    # TODO pokud zbozi neni v nabidce

    # TODO pokud vybrane zbozi neni v nakupnim voziku

    # TODO pokud zbozi uz je v kosiku

    # TODO pokud zbozi neni na sklade

# TODO vypsat obsah kosiku pomoci 'else'
