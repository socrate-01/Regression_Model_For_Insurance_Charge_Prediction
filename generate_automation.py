import pandas as pd
from pydantic import BaseModel, Field
from enum import Enum
import json

# Charger le fichier CSV
csv_file_path = 'insurance.csv'
df = pd.read_csv(csv_file_path, nrows=10, delimiter=';')  # Charger uniquement la première ligne pour l'analyse initiale

# Afficher le contenu du DataFrame
print(df)

# Définir les types pour les colonnes spéciales (Enum)
class SexEnum(str, Enum):
    male = "male"
    female = "female"

class RegionEnum(str, Enum):
    southwest = "southwest"
    southeast = "southeast"
    northwest = "northwest"
    northeast = "northeast"

# Classe Pydantic pour le schéma
class AutoGeneratedSchema(BaseModel):
    pass

# Générer automatiquement les champs en fonction des types de colonnes
for column_name, column_type in df.dtypes.items():
    if pd.api.types.is_numeric_dtype(column_type):
        # Colonnes numériques
        setattr(AutoGeneratedSchema, column_name, Field(None, title=column_name, description=f"{column_name} column."))
    elif pd.api.types.is_bool_dtype(column_type):
        # Colonnes booléennes
        setattr(AutoGeneratedSchema, column_name, Field(None, title=column_name, description=f"{column_name} column."))
    elif pd.api.types.is_object_dtype(column_type):
        # Colonnes de texte
        # Gérer les colonnes spéciales (Enum)
        if df[column_name].nunique() <= 5:  # Arbitrairement défini comme limite pour les colonnes Enum
            enum_class_name = f"{column_name.capitalize()}Enum"
            enum_class = Enum(column_name, df[column_name].unique(), module=__name__)
            globals()[enum_class_name] = enum_class
            setattr(AutoGeneratedSchema, column_name, enum_class)
        else:
            setattr(AutoGeneratedSchema, column_name, Field(None, title=column_name, description=f"{column_name} column."))

# Afficher le code généré
print(json.dumps(AutoGeneratedSchema.model_json_schema(indent=2)))
