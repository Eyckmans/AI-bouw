from fastapi import APIRouter

router = APIRouter()


@router.get("/customers")
def get_customers():
    return {
        "customers": []
    }


@router.post("/customers")
def create_customer(customer: dict):

    return {
        "message": "Klant aangemaakt",
        "customer": customer
    }
