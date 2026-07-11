# Eco-Stock API

API REST développée avec **Django REST Framework** permettant la gestion d'un système de stockage alimentaire.

Cette API centralise la gestion des entrepôts et des produits, avec des règles métier liées au transfert des stocks, un système d'authentification JWT et une architecture basée sur les `ModelViewSet`.

---

# Présentation du projet

Eco-Stock est une plateforme destinée à faciliter la gestion des surplus alimentaires provenant des commerces locaux afin de permettre leur redistribution avant péremption.

L'API permet de gérer :

- les entrepôts de stockage ;
- les produits alimentaires ;
- les relations entre produits et entrepôts ;
- les opérations métier liées au déplacement des stocks ;
- la sécurisation des accès aux données.

---

# Fonctionnalités

## Gestion des entrepôts

- Création d'un entrepôt.
- Consultation des entrepôts.
- Modification d'un entrepôt.
- Suppression d'un entrepôt.
- Audit du nombre de produits présents dans un entrepôt.

## Gestion des produits

- Création d'un produit.
- Consultation des produits.
- Modification d'un produit.
- Suppression d'un produit.
- Association d'un produit à un entrepôt.
- Déplacement d'un produit vers un autre entrepôt.

## Sécurité

- Authentification JWT avec Simple JWT.
- Protection des opérations sensibles avec les permissions DRF.
- Gestion des tokens d'accès et de rafraîchissement.

---

# Technologies utilisées

- Python
- Django 6
- Django REST Framework
- Simple JWT
- SQLite
- CORS Headers
- Postman / Insomnia
- Git

---

# Architecture du projet

```
eco-stock-api/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── inventory/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── manage.py
├── requirements.txt
└── README.md
```

---

# Organisation du code

## Models

Les modèles représentent les entités principales du système.

### Warehouse

```text
id
name
location
capacity
```

### Product

```text
id
name
quantity
expiration_date
status
warehouse
```

Relation :

```
Warehouse (1) --------< (N) Product
```

Un entrepôt peut contenir plusieurs produits.

---

# Logique métier

## Déplacement d'un produit

Endpoint :

```
POST /api/products/{id}/move/
```

Permet de transférer un produit vers un autre entrepôt.

Validation appliquée :

- l'entrepôt de destination doit exister ;
- le champ `warehouse_id` est obligatoire ;
- un produit périmé ne peut pas être déplacé.

Exemple :

```json
{
    "warehouse_id": 2
}
```

Réponse :

```json
{
    "message": "Produit déplacé avec succès."
}
```

---

## Audit d'un entrepôt

Endpoint :

```
GET /api/warehouses/{id}/audit/
```

Retourne le nombre total de produits associés à un entrepôt.

Exemple :

```json
{
    "warehouse": "Entrepôt Paris",
    "total_products": 15
}
```

---

# Authentification JWT

L'API utilise **Simple JWT**.

## Obtenir un token

```
POST /api/token/
```

Réponse :

```json
{
    "access": "token_access",
    "refresh": "token_refresh"
}
```

## Rafraîchir un token

```
POST /api/token/refresh/
```

Les opérations de modification nécessitent une authentification valide.

---

# Documentation des endpoints

## Authentication

| Méthode | Endpoint | Description |
|---|---|---|
| POST | `/api/token/` | Obtenir un token JWT |
| POST | `/api/token/refresh/` | Rafraîchir un token |

---

## Warehouses

| Méthode | Endpoint | Description |
|---|---|---|
| GET | `/api/warehouses/` | Liste des entrepôts |
| POST | `/api/warehouses/` | Créer un entrepôt |
| GET | `/api/warehouses/{id}/` | Détail |
| PUT | `/api/warehouses/{id}/` | Modifier |
| DELETE | `/api/warehouses/{id}/` | Supprimer |
| GET | `/api/warehouses/{id}/audit/` | Audit du stock |

---

## Products

| Méthode | Endpoint | Description |
|---|---|---|
| GET | `/api/products/` | Liste des produits |
| POST | `/api/products/` | Créer un produit |
| GET | `/api/products/{id}/` | Détail |
| PUT | `/api/products/{id}/` | Modifier |
| DELETE | `/api/products/{id}/` | Supprimer |
| POST | `/api/products/{id}/move/` | Déplacer un produit |

---

# Installation

## Cloner le projet

```bash
git clone https://github.com/votre-utilisateur/eco-stock-api.git

cd eco-stock-api
```

## Créer un environnement virtuel

```bash
python -m venv venv
```

Activation :

Windows :

```bash
venv\Scripts\activate
```

Linux / macOS :

```bash
source venv/bin/activate
```

---

## Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## Appliquer les migrations

```bash
python manage.py migrate
```

---

## Créer un utilisateur administrateur

```bash
python manage.py createsuperuser
```

---

## Lancer le serveur

```bash
python manage.py runserver
```

L'API sera disponible sur :

```
http://127.0.0.1:8000/
```

---

# Connexion avec le frontend

L'API autorise les requêtes provenant des applications frontend configurées via CORS.

Frontend Angular :

```
http://localhost:4200
```

---

# Auteur

**Dado Watt**

Projet réalisé dans le cadre d'un développement Full Stack.

Backend :
- Django REST Framework

Frontend associé :
- Angular