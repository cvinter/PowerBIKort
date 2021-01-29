# Python-script for generating maps of the Danish municipalities, that are usable in Power BI.
# To make it easier to read, we make copies of the densely lying Copenhagen municipalities and 
# place them in enlarged version up north.
# The original GeoJSON file is downloaded from https://raw.githubusercontent.com/Neogeografen/dagi/master/geojson/kommuner.geojson
# but there are other nice versions around. We use mapshaper.org to simplify the lines to about 12% and save again as GeoJSON.
# From that file, we manually (in e.g. Notepad++) remove the polygons for Saltholm (Easternmost polygon of Taarnby) and 
# Anholt (Easternmost polygon of Norddjurs). We also manually replace Copenhagen with København throughout

# X is longitude (længdegrad in Danish) and Y is latitude (breddegrader) with East or North being positive direction.
# Denote XMIN and YMIN the values of the smalles X and Y values for the Copenhagen munucipalities. 
# Xoffs and Yoffs are the offsets for moving the copeies of said municipalities while Scale is the factor by which they
# are to be enlarged. New coordinates are then: X' = (X-XMIN)*Scale + Xoffs + XMIN and similar for Y.

# Also, the island of Bornholm is moved by BHxoffs and BHyOffs, so it is placed North of the copied Copenhagen.

# Finally, metadata is added to the polygons about official regions and a more detailed grouping of municipalities than the 
# official regions.

# Using mapshaper.org, the saved copy of the GeoJSON file is saved as TopoJSON which can be imported into Power BI 
# using the preview visual.

import json
import copy # XXX: Denne burde sørge for, man kan kopiere et JSON-object, men det virker vist ikke?

xoffs = -0.8
yoffs = 0.7
scale = 2.8

BHxoffs = -2.6
BHyoffs =  2.4

# XXX Denne skal rettes til din download-placering:
with open("C:\\Users\\dk2371\\OneDrive\\Customers\\Dansk Industri\\Shapemaps\\municipalities_simplificeret_SalthomAnholt.geojson", "r", encoding='utf-8') as read_file:
    komplet = json.load(read_file)
read_file.close()

# XXX: Objektet, der til sidst skal skrives:
komplet_ny = copy.deepcopy(komplet)

københavnerkommuner = ['Dragør','Tårnby','København','Frederiksberg','Hvidovre','Brøndby','Vallensbæk','Albertslund','Glostrup','Rødovre','Ballerup','Herlev','Gladsaxe','Gentofte','Lyngby-Taarbæk','Furesø','Rudersdal','Hørsholm']
bornholmerkommuner = ['Bornholm','Christiansø']

x=[] # Alle længdegrader i Kbh
y=[] # Alle breddegrader i Kbh


# Loop through all polygons to find the smalles coordinates in the Copenhagen municipalities:
for feature in komplet['features']: #Loop over alle polygoner
    geometry = feature['geometry']
    if geometry is not None: # Mapshapers simplificering efterlader tomme polygoner.
        if feature['properties']['label_dk'] in københavnerkommuner:        
            for i in range(len(geometry['coordinates'][0])):
                coordinates=geometry['coordinates'][0][i]
                x.append(coordinates[0])
                y.append(coordinates[1])

# The minima:
xmin = min(x) 
ymin = min(y)


for featurenr in range(len(komplet['features'])):
#    if komplet['features'][featurenr]['geometry'] is not None: # Mapshapers simplificering efterlader tomme polygoner.
    if 1==1:
        kommune = komplet['features'][featurenr]['properties']['label_dk']
        kommune_ny = kommune;
        if   kommune == 'Ballerup'                                   : Region='Region Hovedstaden'   ; DIRegion='DI Hovedstaden'
        elif kommune == 'Bornholm'                                   : Region='Region Hovedstaden'   ; DIRegion='DI Bornholm'
        elif kommune == 'Brøndby'                                    : Region='Region Hovedstaden'   ; DIRegion='DI Hovedstaden'
        elif kommune == 'Brønderslev'                                : Region='Region Nordjylland'   ; DIRegion='DI Vendsyssel'
        elif kommune == 'Fanø'                                       : Region='Region Syddanmark'    ; DIRegion='DI Sydvestjylland'
        elif kommune == 'Faaborg-Midtfyn'                            : Region='Region Syddanmark'    ; DIRegion='DI Fyn'
        elif kommune == 'Helsingør'                                  : Region='Region Hovedstaden'   ; DIRegion='DI Hovedstaden'
        elif kommune == 'Hillerød'                                   : Region='Region Hovedstaden'   ; DIRegion='DI Hovedstaden'
        elif kommune == 'Ikast-Brande'                               : Region='Region Midtjylland'   ; DIRegion='DI Midt Vest'
        elif kommune == 'Ishøj'                                      : Region='Region Hovedstaden'   ; DIRegion='DI Hovedstaden'
        elif kommune == 'Jammerbugt'                                 : Region='Region Nordjylland'   ; DIRegion='DI Aalborg'
        elif kommune == 'Kerteminde'                                 : Region='Region Syddanmark'    ; DIRegion='DI Fyn'
        elif kommune == 'Morsø'                                      : Region='Region Nordjylland'   ; DIRegion='DI Thy/Mors'
        elif kommune == 'Norddjurs'                                  : Region='Region Midtjylland'   ; DIRegion='DI Randers-Norddjurs'
        elif kommune == 'Odsherred'                                  : Region='Region Sjælland'      ; DIRegion='DI VestSjælland'
        elif kommune == 'Ringkøbing-Skjern'                          : Region='Region Midtjylland'   ; DIRegion='DI Midt Vest'
        elif kommune == 'Ringsted'                                   : Region='Region Sjælland'      ; DIRegion='DI VestSjælland'
        elif kommune == 'Slagelse'                                   : Region='Region Sjælland'      ; DIRegion='DI VestSjælland'
        elif kommune == 'Sorø'                                       : Region='Region Sjælland'      ; DIRegion='DI VestSjælland'
        elif kommune == 'Thisted'                                    : Region='Region Nordjylland'   ; DIRegion='DI Thy/Mors'
        elif kommune == 'Vallensbæk'                                 : Region='Region Hovedstaden'   ; DIRegion='DI Hovedstaden'
        elif kommune == 'Varde'                                      : Region='Region Syddanmark'    ; DIRegion='DI Sydvestjylland'
        elif kommune == 'Vejle'                                      : Region='Region Syddanmark'    ; DIRegion='DI Trekantområdet'
        elif kommune == 'Vordingborg'                                : Region='Region Sjælland'      ; DIRegion='DI SydSjælland'
        elif kommune == 'Ærø'                                        : Region='Region Syddanmark'    ; DIRegion='DI Fyn'
        elif kommune == 'Aabenraa'                                   : Region='Region Syddanmark'    ; DIRegion='DI Sønderjylland'
        elif kommune == 'Aalborg'                                    : Region='Region Nordjylland'   ; DIRegion='DI Aalborg'
        elif kommune == 'Aarhus'                                     : Region='Region Midtjylland'   ; DIRegion='DI Østjylland'
        elif kommune == 'Dragør'                                     : Region='Region Hovedstaden'   ; DIRegion='DI Hovedstaden'
        elif kommune == 'Faxe'                                       : Region='Region Sjælland'      ; DIRegion='DI SydSjælland'
        elif kommune == 'Fredericia'                                 : Region='Region Syddanmark'    ; DIRegion='DI Trekantområdet'
        elif kommune == 'Glostrup'                                   : Region='Region Hovedstaden'   ; DIRegion='DI Hovedstaden'
        elif kommune == 'Gribskov'                                   : Region='Region Hovedstaden'   ; DIRegion='DI Hovedstaden'
        elif kommune == 'Guldborgsund'                               : Region='Region Sjælland'      ; DIRegion='DI Lolland-Falster'
        elif kommune == 'Holbæk'                                     : Region='Region Sjælland'      ; DIRegion='DI VestSjælland'
        elif kommune == 'Horsens'                                    : Region='Region Midtjylland'   ; DIRegion='DI Horsens'
        elif kommune == 'Høje-Taastrup'                              : Region='Region Hovedstaden'   ; DIRegion='DI Hovedstaden'
        elif kommune == 'Kalundborg'                                 : Region='Region Sjælland'      ; DIRegion='DI VestSjælland'
        elif kommune == 'Kolding'                                    : Region='Region Syddanmark'    ; DIRegion='DI Trekantområdet'
        elif kommune == 'Lemvig'                                     : Region='Region Midtjylland'   ; DIRegion='DI Midt Vest'
        elif kommune == 'Middelfart'                                 : Region='Region Syddanmark'    ; DIRegion='DI Trekantområdet'
        elif kommune == 'Nordfyn'                                    : Region='Region Syddanmark'    ; DIRegion='DI Fyn'; kommune_ny = 'Nordfyns'
        elif kommune == 'Næstved'                                    : Region='Region Sjælland'      ; DIRegion='DI SydSjælland'
        elif kommune == 'Skive'                                      : Region='Region Midtjylland'   ; DIRegion='DI Midt Vest'
        elif kommune == 'Stevns'                                     : Region='Region Sjælland'      ; DIRegion='DI SydSjælland'
        elif kommune == 'Struer'                                     : Region='Region Midtjylland'   ; DIRegion='DI Midt Vest'
        elif kommune == 'Svendborg'                                  : Region='Region Syddanmark'    ; DIRegion='DI Fyn'
        elif kommune == 'Vesthimmerland'                             : Region='Region Nordjylland'   ; DIRegion='DI Aalborg'; kommune_ny = 'Vesthimmerlands'
        elif kommune == 'Viborg'                                     : Region='Region Midtjylland'   ; DIRegion='DI Silkeborg-Viborg'
        elif kommune == 'Albertslund'                                : Region='Region Hovedstaden'   ; DIRegion='DI Hovedstaden'
        elif kommune == 'Assens'                                     : Region='Region Syddanmark'    ; DIRegion='DI Fyn'
        elif kommune == 'Billund'                                    : Region='Region Syddanmark'    ; DIRegion='DI Sydvestjylland'
        elif kommune == 'Christiansø'                                : Region='Region Hovedstaden'   ; DIRegion='DI Bornholm'
        elif kommune == 'Favrskov'                                   : Region='Region Midtjylland'   ; DIRegion='DI Østjylland'
        elif kommune == 'Fredensborg'                                : Region='Region Hovedstaden'   ; DIRegion='DI Hovedstaden'
        elif kommune == 'Frederiksberg'                              : Region='Region Hovedstaden'   ; DIRegion='DI Hovedstaden'
        elif kommune == 'Furesø'                                     : Region='Region Hovedstaden'   ; DIRegion='DI Hovedstaden'
        elif kommune == 'Gentofte'                                   : Region='Region Hovedstaden'   ; DIRegion='DI Hovedstaden'
        elif kommune == 'Gladsaxe'                                   : Region='Region Hovedstaden'   ; DIRegion='DI Hovedstaden'
        elif kommune == 'Greve'                                      : Region='Region Sjælland'      ; DIRegion='DI Roskilde/Køge Bugt'
        elif kommune == 'Halsnæs'                                    : Region='Region Hovedstaden'   ; DIRegion='DI Hovedstaden'
        elif kommune == 'Hedensted'                                  : Region='Region Midtjylland'   ; DIRegion='DI Horsens'
        elif kommune == 'Hjørring'                                   : Region='Region Nordjylland'   ; DIRegion='DI Vendsyssel'
        elif kommune == 'Hvidovre'                                   : Region='Region Hovedstaden'   ; DIRegion='DI Hovedstaden'
        elif kommune == 'Hørsholm'                                   : Region='Region Hovedstaden'   ; DIRegion='DI Hovedstaden'
        elif kommune == 'København'                                  : Region='Region Hovedstaden'   ; DIRegion='DI Hovedstaden'; kommune_ny = 'København'
        elif kommune == 'Lejre'                                      : Region='Region Sjælland'      ; DIRegion='DI Roskilde/Køge Bugt'
        elif kommune == 'Lolland'                                    : Region='Region Sjælland'      ; DIRegion='DI Lolland-Falster'
        elif kommune == 'Lyngby-Taarbæk'                             : Region='Region Hovedstaden'   ; DIRegion='DI Hovedstaden'
        elif kommune == 'Læsø'                                       : Region='Region Nordjylland'   ; DIRegion='DI Vendsyssel'
        elif kommune == 'Odder'                                      : Region='Region Midtjylland'   ; DIRegion='DI Horsens'
        elif kommune == 'Odense'                                     : Region='Region Syddanmark'    ; DIRegion='DI Fyn'
        elif kommune == 'Rebild'                                     : Region='Region Nordjylland'   ; DIRegion='DI Aalborg'
        elif kommune == 'Rudersdal'                                  : Region='Region Hovedstaden'   ; DIRegion='DI Hovedstaden'
        elif kommune == 'Rødovre'                                    : Region='Region Hovedstaden'   ; DIRegion='DI Hovedstaden'
        elif kommune == 'Samsø'                                      : Region='Region Midtjylland'   ; DIRegion='DI Horsens'
        elif kommune == 'Silkeborg'                                  : Region='Region Midtjylland'   ; DIRegion='DI Silkeborg-Viborg'
        elif kommune == 'Skanderborg'                                : Region='Region Midtjylland'   ; DIRegion='DI Østjylland'
        elif kommune == 'Allerød'                                    : Region='Region Hovedstaden'   ; DIRegion='DI Hovedstaden'
        elif kommune == 'Egedal'                                     : Region='Region Hovedstaden'   ; DIRegion='DI Hovedstaden'
        elif kommune == 'Esbjerg'                                    : Region='Region Syddanmark'    ; DIRegion='DI Sydvestjylland'
        elif kommune == 'Frederikshavn'                              : Region='Region Nordjylland'   ; DIRegion='DI Vendsyssel'
        elif kommune == 'Frederikssund'                              : Region='Region Hovedstaden'   ; DIRegion='DI Hovedstaden'
        elif kommune == 'Haderslev'                                  : Region='Region Syddanmark'    ; DIRegion='DI Sønderjylland'
        elif kommune == 'Herlev'                                     : Region='Region Hovedstaden'   ; DIRegion='DI Hovedstaden'
        elif kommune == 'Herning'                                    : Region='Region Midtjylland'   ; DIRegion='DI Midt Vest'
        elif kommune == 'Holstebro'                                  : Region='Region Midtjylland'   ; DIRegion='DI Midt Vest'
        elif kommune == 'Køge'                                       : Region='Region Sjælland'      ; DIRegion='DI Roskilde/Køge Bugt'
        elif kommune == 'Langeland'                                  : Region='Region Syddanmark'    ; DIRegion='DI Fyn'
        elif kommune == 'Mariagerfjord'                              : Region='Region Nordjylland'   ; DIRegion='DI Aalborg'
        elif kommune == 'Nyborg'                                     : Region='Region Syddanmark'    ; DIRegion='DI Fyn'
        elif kommune == 'Randers'                                    : Region='Region Midtjylland'   ; DIRegion='DI Randers-Norddjurs'
        elif kommune == 'Roskilde'                                   : Region='Region Sjælland'      ; DIRegion='DI Roskilde/Køge Bugt'
        elif kommune == 'Solrød'                                     : Region='Region Sjælland'      ; DIRegion='DI Roskilde/Køge Bugt'
        elif kommune == 'Syddjurs'                                   : Region='Region Midtjylland'   ; DIRegion='DI Østjylland'
        elif kommune == 'Sønderborg'                                 : Region='Region Syddanmark'    ; DIRegion='DI Sønderjylland'
        elif kommune == 'Tønder'                                     : Region='Region Syddanmark'    ; DIRegion='DI Sønderjylland'
        elif kommune == 'Tårnby'                                     : Region='Region Hovedstaden'   ; DIRegion='DI Hovedstaden'
        elif kommune == 'Ukendt'                                     : Region='Ukendt'               ; DIRegion='Ukendt'
        elif kommune == 'Vejen'                                      : Region='Region Syddanmark'    ; DIRegion='DI Sydvestjylland'

        komplet['features'][featurenr]['properties']['RegionNavn'] = Region
        komplet['features'][featurenr]['properties']['DIRegionNavn'] = DIRegion
        komplet_ny['features'][featurenr]['properties']['RegionNavn'] = Region
        komplet_ny['features'][featurenr]['properties']['DIRegionNavn'] = DIRegion
        komplet_ny['features'][featurenr]['properties']['label_dk'] = kommune_ny
        komplet_ny['features'][featurenr]['properties']['label_en'] = kommune_ny

        if kommune in københavnerkommuner: #Copied and scaled
            komplet_ny['features'].append(komplet['features'][featurenr])
            for i in range(len(komplet['features'][featurenr]['geometry']['coordinates'][0])):
                x  = komplet['features'][featurenr]['geometry']['coordinates'][0][i][0]
                y  = komplet['features'][featurenr]['geometry']['coordinates'][0][i][1]
                komplet_ny['features'][featurenr]['geometry']['coordinates'][0][i][0] = (x - xmin)*scale + xoffs + xmin
                komplet_ny['features'][featurenr]['geometry']['coordinates'][0][i][1] = (y - ymin)*scale + yoffs + ymin
        if komplet['features'][featurenr]['properties']['label_dk'] in bornholmerkommuner: #Just moved
            for i in range(len(komplet['features'][featurenr]['geometry']['coordinates'][0])): #Flyttes
                komplet_ny['features'][featurenr]['geometry']['coordinates'][0][i][0] = komplet['features'][featurenr]['geometry']['coordinates'][0][i][0] + BHxoffs
                komplet_ny['features'][featurenr]['geometry']['coordinates'][0][i][1] = komplet['features'][featurenr]['geometry']['coordinates'][0][i][1] + BHyoffs                        

with open("C:\\Users\dk2371\\OneDrive\\Customers\Dansk Industri\\Shapemaps\\municipalities_simplificeret_KbhFlyttet.geojson", 'w') as outfile:
    json.dump(komplet_ny, outfile)


