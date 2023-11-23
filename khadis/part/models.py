from django.db import models

class H_Kitoblar(models.Model):

    lotin = models.CharField(max_length=60)
    arab = models.CharField(max_length=60)
    haqida = models.TextField(max_length=2000)

    def __str__(self):
        return self.lotin
    
class H_Qismlar(models.Model):
    kitobdan = models.ForeignKey(H_Kitoblar , on_delete=models.CASCADE)
    lotin = models.CharField(max_length=100)
    arab = models.CharField(max_length=100)
    dan = models.IntegerField(default=0)
    gacha = models.IntegerField(default=1)


    def __str__(self):
        return self.lotin


class Q_Parchalar(models.Model):
    qismdan = models.ForeignKey(H_Qismlar ,on_delete= models.CASCADE)
    lotin = models.CharField(max_length=100)
    arab = models.CharField(max_length=100)

    def __str__(self):
        return self.lotin

class V_Hadislar(models.Model):
    parchadan = models.ForeignKey(Q_Parchalar ,on_delete=models.CASCADE)
    lotin = models.CharField(max_length=2000)
    arab = models.CharField(max_length=2000)
    toifa = models.CharField(max_length=100 ,default='Sahih')
    tomonidan = models.CharField(max_length=100 ,default='by Someone')
    kitobda = models.CharField(max_length=100, default='1 qism 4 bet 3 hadis')


    def __str__(self):
        return self.lotin


# H_Kitoblar
# K_Qismlar
# Q_Parchalar
# Hadislar
