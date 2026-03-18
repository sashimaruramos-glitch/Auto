from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class PricingRules(Base):
    __tablename__ = 'pricing_rules'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)

    def __repr__(self):
        return f'<PricingRules(id={self.id}, name={self.name}, amount={self.amount})>'

class PrintJobs(Base):
    __tablename__ = 'print_jobs'

    id = Column(Integer, primary_key=True)
    job_name = Column(String, nullable=False)
    pricing_rule_id = Column(Integer, ForeignKey('pricing_rules.id'), nullable=False)

    pricing_rule = relationship('PricingRules', back_populates='print_jobs')

    def __repr__(self):
        return f'<PrintJobs(id={self.id}, job_name={self.job_name})>'

PricingRules.print_jobs = relationship('PrintJobs', order_by=PrintJobs.id, back_populates='pricing_rule')