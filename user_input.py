from pydantic import BaseModel, Field, field_validator, computed_field
from typing_extensions import Annotated 

from train.city_tier import tier_1_cities, tier_2_cities




# pydantic model for 'post'

class rule_post(BaseModel):
    age: Annotated[int, Field(..., description='Enter your age',gt=0)]
    weight: Annotated[float, Field(..., description='Enter your weight (kg)', gt=0.0)]
    height: Annotated[float, Field(..., description='Enter your height (m)', gt=0, lt=2.5)]
    income_lpa: Annotated[float, Field(..., description='Enter your income (lpa)', ge=0.0)]
    smoker: Annotated[bool, Field(..., description='Are you a smoker? (T/F)')]
    city: Annotated[str, Field(..., description='Enter your city name')]
    occupation: Annotated[str,Field(..., description='Enter your occupation type')]


    # validate 'occupation'
    @field_validator('occupation')
    @classmethod
    def occupation_validator(cls, occupation):
        occupation_class = ['retired', 'freelancer', 'student', 'government_job','business_owner', 'unemployed', 'private_job']
        if occupation.lower() in occupation_class:
            return occupation
        raise ValueError(f'Invalid type ❌. Choose from {occupation_class}')
    

    # validate 'city'
    @field_validator('city')
    @classmethod
    def validate_city(cls, city):
        city = city.strip().title()
        return city



    # compute 'bmi'
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height**2),2)
        return bmi
    

    # compute 'age_group'
    @computed_field    
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"       


    # compute lifestyle_risk
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"
        

    
    # compute 'city_tier'
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3
   










