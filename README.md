# Eco-Stock API

## Présentation du projet

Eco-Stock est une API REST développée avec Django REST Framework. Elle permet de gérer un système de stock alimentaire entre plusieurs entrepôts dans le cadre d'une plateforme de redistribution de produits alimentaires proches de leur date de péremption.

L'objectif de cette API est de centraliser la gestion des produits, de suivre leur état, de gérer leur localisation dans différents entrepôts et d'assurer des opérations métier comme le transfert de produits et l'audit des stocks.

## Fonctionnalités

- Gestion des entrepôts (Warehouse)
- Gestion des produits (Product)
- Suivi du statut des produits (disponible, réservé, périmé)
- Transfert de produits entre entrepôts
- Audit des entrepôts (nombre total de produits)
- API sécurisée avec authentification JWT

## Installation du projet

### 1. Cloner le projet

```bash
git clone <url_du_repo>
cd eco-stock

```
### 2. Créer un environnement virtuel
python -m venv .venv

### 3. Activer l'environnement

Sous Windows :

.venv\Scripts\activate
### 4. Installer les dépendances
pip install -r requirements.txt

### 5. Appliquer les migrations
python manage.py makemigrations
python manage.py migrate

### 6. Créer un super utilisateur
python manage.py createsuperuser

### 7. Lancer le serveur
python manage.py runserver


## Authentification JWT

L'API utilise JWT pour sécuriser les routes.

## Obtenir un token
POST /api/token/

Body :

{
    "username": "admin",
    "password": "password"
}

## Rafraîchir le token
POST /api/token/refresh/

## Endpoints de l'API

## Produits
GET /api/products/
POST /api/products/
GET /api/products/{id}/
PUT /api/products/{id}/
DELETE /api/products/{id}/
POST /api/products/{id}/move/

## Entrepôts
GET /api/warehouses/
POST /api/warehouses/
GET /api/warehouses/{id}/
PUT /api/warehouses/{id}/
DELETE /api/warehouses/{id}/
GET /api/warehouses/{id}/audit/

## Règles métier
Un produit périmé ne peut pas être منتقلé vers un autre entrepôt
L’audit d’un entrepôt retourne le nombre total de produits associés
Seuls les utilisateurs authentifiés peuvent modifier les données (création, modification, suppression)

## Sécurité

L’API est sécurisée via JWT (JSON Web Token). Les utilisateurs doivent s’authentifier pour obtenir un token, qui doit ensuite être envoyé dans l’en-tête Authorization pour accéder aux routes protégées.

Format :

Authorization: Bearer <access_token>

## Technologies utilisées
- Python
- Django
- Django REST Framework
- Simple JWT
- SQLite (ou autre base configurée)

