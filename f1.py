import logging

logging.basicConfig(level=10,filename='log2.txt',filemode='a',format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p')


while True:
    print("1.age_checked\n2.covid_checked\n3.vaccination status")
    choice=int(input('Enter your choice: '))
    logging.info(f"choice process{choice}")
    if choice==1:
        logging.info('Age checking done')
    elif choice==2:
        logging.info('covid checking done')
    elif choice==3:
        logging.info('vaccination status checked')
    else:
        logging.error('invalid input checked')
        try:
            ch=int(input('Do you want to continie [5|6]: '))
            if ch==6:
                logging.info('Application closed')
                break
        except ValueError  as msg:
            logging.exception(msg)


