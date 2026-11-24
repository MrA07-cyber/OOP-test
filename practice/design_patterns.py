"""AI-assisted study examples for seven design patterns."""
from dataclasses import dataclass
from functools import wraps
import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


# Factory: choose a payment fee calculation.
class Card:
    def fee(self, amount):
        return round(amount * 0.029, 2)


class Transfer:
    def fee(self, amount):
        return 1.50


class PayPal:
    def fee(self, amount):
        return round(amount * 0.034 + 0.30, 2)


def payment_processor(method):
    return {"card": Card, "transfer": Transfer, "paypal": PayPal}[method]()


# Builder: assemble an employee record in stages.
@dataclass(frozen=True)
class Employee:
    name: str
    department: str
    laptop: bool = False


class EmployeeBuilder:
    def __init__(self, name):
        self.data = {"name": name, "department": "General"}

    def department(self, value):
        self.data["department"] = value
        return self

    def laptop(self, enabled=True):
        self.data["laptop"] = enabled
        return self

    def build(self):
        return Employee(**self.data)


# Singleton: shared settings.
class Settings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.values = {}
        return cls._instance


# Adapter: translate a legacy XML record into JSON.
class XMLAdapter:
    def convert(self, source):
        root = ET.fromstring(source)
        return json.dumps({node.tag: node.text for node in root})


# Decorator: wrap a price calculation with an extra charge.
def surcharge(amount):
    def decorate(price):
        @wraps(price)
        def calculate(*args, **kwargs):
            return price(*args, **kwargs) + amount
        return calculate
    return decorate


# Strategy: choose the report format at runtime.
class Report:
    def __init__(self, formatter):
        self.formatter = formatter

    def render(self, data):
        return self.formatter(data)


# Template method: keep the order of pipeline steps fixed.
class Pipeline(ABC):
    def run(self, source):
        return self.load(self.transform(self.extract(source)))

    @abstractmethod
    def extract(self, source):
        pass

    def transform(self, rows):
        return [row.strip() for row in rows if row.strip()]

    def load(self, rows):
        return rows


class TextPipeline(Pipeline):
    def extract(self, source):
        return source.splitlines()
