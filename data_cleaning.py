import os 
import pandas as pd

def preparation_data(path): 
    
    df_subventions = pd.read_csv(os.path.join(path, 'subventions-accordees-et-refusees.csv'), sep=";")
   

    df_subventions = df_subventions.rename({'Numéro de dossier': 'id' , 'Année budgétaire': 'annee_vote' , 'Collectivité':'collectivite', 'Nom Bénéficiaire':'nom_beneficiaire', 'Numéro Siret':'siret', 'Objet du dossier':'objet', 'Montant voté':'montant', 'Direction':'direction', 'Nature de la subvention':'type_subvention', 'Secteurs d\'activités définies par l\'association':'activite_association'}, axis = 'columns')

 
    
        
    return df_subventions
 
        