from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Modelo para la tabla Categories
class Category(Base):
    __tablename__ = 'categories'

    category_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    # Relación con la tabla Questions
    questions = relationship("Question", back_populates="category")

# Modelo para la tabla Questions
class Question(Base):
    __tablename__ = 'questions'

    question_id = Column(Integer, primary_key=True, autoincrement=True)
    question_text = Column(Text, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    difficulty_level = Column(String(20))

    # Relación con la tabla Categories y Answers
    category = relationship("Category", back_populates="questions")
    answers = relationship("Answer", back_populates="question")

# Modelo para la tabla Answers
class Answer(Base):
    __tablename__ = 'answers'

    answer_id = Column(Integer, primary_key=True, autoincrement=True)
    answer_text = Column(Text, nullable=False)
    is_correct = Column(Boolean, nullable=False)
    question_id = Column(Integer, ForeignKey('questions.question_id'))

    # Relación con la tabla Questions
    question = relationship("Question", back_populates="answers")

