#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>
struct patient{
    int id;
    char patientname[50];
    char patientaddress[50];
    char disease[50];
    char date[12];
}p;

struct doctor{
    int id;
    char name[50];
    char address[50];
    char specialize[50];
    char date[50];
}d;
void admitPatient();
void patientList();
void dischargePatient();
void addDoctor();
void doctorList();


FILE *fp;

int main(){
int ch;
while(1){
    system("cls");
    printf("<== HOSPITAL MANAGEMENT SYSTEM ==> \n");
    printf("1.Admit Patient\n");
    printf("2.Patient List\n");
    printf("3.Discharge Patient\n");
    printf("4.Add Doctor\n");
    printf("5.Doctors List\n");
    printf("0.Exit\n\n");
    printf("Enter your choice : ");
    scanf("%d",&ch);

    switch(ch){
        case 0:
            exit(0);
        case 1:
            admitPatient( );
            break;
        case 2:
            patientList( );
            break;
        case 3:
            dischargePatient();
            break;
        case 4:
            addDoctor();
            break;
        case 5:
            doctorList();
            break;
        default:
            printf("\nInvalid Choice!! Please Enter Again.\n\n");
    }
    printf("\n\n ENTER ANY KEY TO CONTINUE . . .  ");
    getchar();
    getchar();

}
    return 0;
}

void  admitPatient(){
    char myDate[12];
    time_t t = time(NULL);
    struct tm tm  = *localtime(&t);
    sprintf(myDate, "%02d/%02d/%d" , tm.tm_mday , tm.tm_mon+1 , tm.tm_year+1900 );
    strcpy(p.date,myDate);

    fp= fopen("patient.txt","ab");
    if (fp == NULL) {
        printf("Error opening patient file.\n");
        return;
    }

    printf("Enter Patient ID : ");
    scanf("%d",&p.id);

    printf("Enter Patient Name : ");
    fflush(stdin);
    fgets(p.patientname,50,stdin);
    p.patientname[strcspn(p.patientname, "\n")] = '\0';

    printf("Enter Patient's Address : ");
    fflush(stdin);
    fgets(p.patientaddress,50,stdin);
    p.patientaddress[strcspn(p.patientaddress, "\n")] = '\0';

    printf("Enter Patient Disease : ");
    fflush(stdin);
    fgets(p.disease,50,stdin);
    p.disease[strcspn(p.disease, "\n")] = '\0';

    printf("PATIENT ADDED SUCCESSFULLY...");

    fwrite(&p,sizeof(p),1,fp);
    fclose(fp);
}

void patientList(){
    system("cls");
    printf("<==PATIENT LIST==>\n");
    printf("%-10s %-30s %-30s %-20s %s\n","Id" , "Patient Name" , "Patient Address" , "Disease" , "Date");
    printf("===============================================================================================================\n");

    fp=fopen("patient.txt","rb");
    if(fp == NULL) {
        printf("Error opening patient file.\n");
        return;
    }
    while(fread(&p,sizeof(p),1,fp)==1){
        printf("%-10d %-30s %-30s %-20s %s\n",p.id , p.patientname , p.patientaddress , p.disease , p.date);
    }
    fclose(fp);
}


void dischargePatient(){
    int id , f=0;

    system("cls");
    printf("<==DISCHAGE PATIENT==>\n");
    printf("Enter Patient Id to be Discharged: ");
    scanf("%d",&id);

    FILE *ft;
    fp=fopen("patient.txt" , "rb");
    if (fp == NULL) {
        printf("Error opening patient file.\n");
        return;
    }
    ft=fopen("temp.txt" , "wb");
    if (ft == NULL) {
        printf("Error opening temporary file.\n");
        fclose(fp);
        return;
    }


    while(fread(&p , sizeof(p) , 1 , fp)==1) {
        if (id == p.id){
            f=1;
        }
        else{
            fwrite( &p , sizeof(p) , 1, ft );
        }
    }

    if(f==1){
        printf("\n\n PATIENT DISCHARGED SUCCESSFULLY . . .");
    }
    else{
        printf("\n\nNO RECORDS FOUND . . .");
    }

    fclose(fp);
    fclose(ft);


    remove( "patient.txt") ;
    rename ("temp.txt" , "patient.txt" ) ;


}

void addDoctor(){
    char myDate[12];
    time_t t = time(NULL);
    struct tm tm = *localtime(&t);
    sprintf(myDate,"%02d/%02d/%d" , tm.tm_mday , tm.tm_mon+1 , tm.tm_year+1900);
    strcpy(d.date,myDate);


    int f=0;
    system("cls");
    printf("<==ADD DOCTOR==>\n\n");

    fp = fopen("doctor.txt","ab");

    printf("Enter Doctor's Id : ");
    scanf("%d" , &d.id);

    printf("Enter Doctor's Name : ");
    fflush(stdin);
    fgets(d.name,50,stdin);
    d.name[strcspn(d.name, "\n")] = '\0';

    printf("Enter Doctor's Address : ");
    fflush(stdin);
    fgets(d.address,50,stdin);
    d.address[strcspn(d.address, "\n")] = '\0';

    printf("Doctor Specialize in : ");
    fflush(stdin);
    fgets(d.specialize,50,stdin);
    d.specialize[strcspn(d.specialize, "\n")] = '\0';

    printf("DOCTOR ADDED SUCCESSFULLY . . .");

    fwrite( &d , sizeof(d) ,  1 , fp );
    fclose(fp);


}


void doctorList(){
    system("cls");
    printf("<==DOCTOR LIST==>\n");
    printf("%-10s %-30s %-30s %-30s %s\n","Id" , "Doctor Name" , "Doctor Address" , "Specialize" , "Date");
    printf("===============================================================================================================\n");

    fp=fopen("doctor.txt","rb");
    if(fp == NULL) {
        printf("Error opening doctor file.\n");
        return;
    }
    while(fread(&d,sizeof(d),1,fp)==1){
        printf("%-10d %-30s %-30s %-30s %s\n",d.id , d.name , d.address , d.specialize , d.date);
    }
    fclose(fp);
}
