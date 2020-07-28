from django.db import models

# Create your models here.

class Pet(models.Model):
  LABRADOR = 'LAB'
  BULDOGUE = 'BUL'
  POODLE = 'POO'
  PASTOR_ALEMAO = 'PAS'
  BEAGLE = 'BEA'
  GOLDEN_RETRIEVER = 'GOL'
  CHIHUAHUA = 'CHI'
  HUSKY_SIBERIANO = 'HUS'

  RACA_CHOICES = (
    (LABRADOR, 'Labrador'),
    (BULDOGUE, 'Buldogue'),
    (POODLE, 'Poodle'),
    (PASTOR_ALEMAO, 'Pastor Alemão'),
    (BEAGLE, 'Beagle'),
    (GOLDEN_RETRIEVER, 'Golden Retriever'),
    (CHIHUAHUA, 'Chihuahua'),
    (HUSKY_SIBERIANO, 'Husky Siberiano')
  )

  nome = models.CharField(max_length=30)
  raca = models.CharField(max_length=3, choices=RACA_CHOICES)
  idade = models.IntegerField(default=0)

  def get_choice_name(self, choice):
    name = ''
    for i in range(len(self.RACA_CHOICES)):
      current_choice = self.RACA_CHOICES.__getitem__(i)
      if choice == current_choice[0]:
        name = current_choice[1]
        break
    return name

  def __str__(self):
    return '{} - {} - {}'.format(self.nome, self.get_choice_name(self.raca), self.idade)

