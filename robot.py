class Robot1:
    def __init__(self, name, nomer=None, dom=None, sarai=None, dob_itaz=None, snesty=None):
        self.nomer=nomer
        self.name=name
        self.dom=dom
        self.sarai=sarai
        self.dob_itaz=dob_itaz
        self.snesty=snesty

robot_B=Robot1(nomer='АА001221-56', name='B')
print('Создан робот с именем',robot_B.name,'под номером',robot_B.nomer)

print('\nРобот не умеет ничего выполнять, поэтому отправим его на обучение')
robot_Buta=Robot1(nomer='АА001221-56', name='ВИТА.', dom='строить дом', sarai='строить сарай')
print('После обучения робот полчил имя',robot_Buta.name,'Теперь он умеет', robot_Buta.dom,'и', robot_Buta.sarai)

print('\nДля повышения функций робота, отправим его на предприятие ООО Кошмарик')
robot_Butaliy=Robot1(name='Виталий.',dob_itaz='добавлять этаж', snesty='сносить этаж')
print('После эксплуатации на предприятии, ему дали имя', robot_Butaliy.name,'' 'Он научился', robot_Butaliy.dob_itaz,'и',robot_Butaliy.snesty)

print('\nПосле всего процесса обучения, Виталий умеет:')
print(robot_Buta.dom,', ', robot_Buta.sarai,', ', robot_Butaliy.dob_itaz,', ', robot_Butaliy.snesty, sep='')
