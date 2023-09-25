class Sistema:
    bicicletas_diponibles={1:"B1",
    2:"B2",                           
    3:"B3",
    4:"B4",
    5:"B5",
    6:"B6",
    7:"B7",
    8:"B8"}
    

    bicicletas_en_uso=[]
    

    def ver_bicicletas(self):
        for x in self.bicicletas_diponibles.values():
            print(x)





    def alquilar(self,seleccion):
        clave_a_mover=None
        for clave, seleccion in self.bicicletas_diponibles.items():
            if seleccion == seleccion_a_mover:
                clave_a_mover==clave
        if clave_a_mover is not None:
            self.bicicletas_en_uso[clave_a_mover]=seleccion_a_mover
            del self.bicicletas_diponibles[clave_a_mover]

       
    
         
    





        