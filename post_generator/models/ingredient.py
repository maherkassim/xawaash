from django.db import models
from post_generator.models import DictionaryItem, IngredientBlock, TextBlock

class Ingredient(models.Model):
    ingredient_block = models.ForeignKey(IngredientBlock)
    
    name = models.ForeignKey(
        DictionaryItem,
        related_name="name",
        limit_choices_to={'_set':'General'},
    )
    
    size = models.ForeignKey(
        DictionaryItem,
        related_name="size",
        null=True,
        blank=True,
        limit_choices_to={'_set':'Size'},
    )
    
    quantity = models.CharField(
        'Quantity',
        max_length=20,
        blank=True,
    )
    
    quantity_units = models.ForeignKey(
        DictionaryItem,
        related_name="quantity_units",
        null=True,
        blank=True,
        limit_choices_to={'_set':'Quant_Unit'},
    )
    
    intl = models.CharField(
        'International Quantity',
        max_length=20,
        blank=True,
    )
    
    intl_units = models.ForeignKey(
        DictionaryItem,
        related_name="intl_units",
        verbose_name="International Units",
        null=True,
        blank=True,
        limit_choices_to={'_set':'Intl_Unit'},
    )
    
    prep_style = models.ManyToManyField(
        DictionaryItem,
        related_name='prep_style',
        verbose_name='Preparation Methods/Styles',
        null=True,
        blank=True,
        limit_choices_to={'_set':'Prep_Type'},
    )
    
    comment = models.ForeignKey(
        TextBlock,
        related_name="comment",
        null=True,
        blank=True,
    ) 
    
    optional = models.BooleanField()
    
    class Meta:
        app_label = 'post_generator'
    
    def __unicode__(self):
        return self.ingredient_block.post.title.english.title() + ' - ' + self.ingredient_block.header.english.title() + ' - ' + self.name.english
