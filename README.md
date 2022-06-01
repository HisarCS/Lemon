# Lemon Robot

Merhabalar! Burada Lemon robotun kodunu açıklayacağız.
## Bazı gereken bilgiler
8 thread olsa simultanious bacak çalıştırabilecektik
### important: eğer simultaneous olayı olmazsa thread start ettiğin gibi lock et sonra ikinci thread start ettiğinden emin olduğunda ikisini release et. 
çağırdığın metodda queque argumanı aç ondan sonra ana modulunde bir queque objesi açıyorsun bir argüman olarak yaratıyorsun secondary obje yaratırken o arguman queque ya değer atıyorsun sonra o değeri de asıl queque!yu açtığın modülden geri alıyorsun böylelikle thread!i safe bir şekilde kapatabiliyorsun
# Import
Kodumuzda micropython'da mevcut olan başka kütüphaneleri de kullanmaktayız. Bu kütüphaneler parçaları bağladığımız pin değerlerini, arada kullandığımız sleep kodunu, pwm ve uart sinyallerini kullanmamızı sağlar.

![image](https://user-images.githubusercontent.com/63399574/168583907-c8968cf0-1d5c-4f9e-a673-e1d1f8e01f90.png)

# Parçaları tanımlama
![image](https://user-images.githubusercontent.com/63399574/168582937-970195a6-95b1-4179-b61b-a7cc64d397f1.png)

## Değişkenler
kodun içinde bir çok yerde değişken kullanmaktayız, bunlardan önemli 2'si position ve pos'dur.

![image](https://user-images.githubusercontent.com/63399574/168583217-9bc4b848-a462-43c8-8375-75b5fbf20a6b.png)
bunlar femur ve tibia'nın hareketinde kullandığımız değerleri loop'un dışında tanımlamamızı sağlar.

# Metodlar
2 tane metod tanımladık, birisi ultrasonik sensörümüzle mesafe ölçmemizi sağlayan dist, öbürü ise küçük bir teknik detaydan dolayı servoların titremesini engelleyen stop metodudur.

![image](https://user-images.githubusercontent.com/63399574/168583556-341ae35c-86e5-40fa-a6b5-6336cdc6f90b.png)


# Değişkenler

# Loop'lar

# Komutlar ve ne işe yaradıkları
