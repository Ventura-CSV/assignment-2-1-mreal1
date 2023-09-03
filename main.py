def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    males = input('Please enter number of males: ')
    females = input('Please enter number of females: ')
    total_stu = int(males) + int(females)
    m_perc = (int(males) / int(total_stu)) * 100
    f_perc = (int(females) / int(total_stu)) *100
    print(f'The percentage of males and females: \t {m_perc} \t {f_perc}')
    print(total_stu)
    print(m_perc + f_perc)
    print (f'some message \t {f_perc:.2f}')                      
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
