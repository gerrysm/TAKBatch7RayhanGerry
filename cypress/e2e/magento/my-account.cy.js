describe("My Account Edit Account", () => {
    beforeEach(() => {
      cy.visit(
        "https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/"
      );
    });

    it("My Account Edit Account", () => {
        cy.get('[name="login[username]"]').type("akram@yahoo.com");
        cy.get('[name="login[password]"]').type("Bajubaru22");
        cy.get("#send2").click();
        cy.wait(15000);
        cy.get(':nth-child(2) > .customer-welcome > .customer-name > .action').click();

        cy.get(':nth-child(2) > .customer-welcome > .customer-menu > .header > :nth-child(1) > a').click();
        
        cy.get('.block-dashboard-info > .block-content > .box > .box-actions > .edit > span').click();
        
        
        cy.get('#firstname').clear();

     
        cy.get('#firstname').type("Akram India");
        cy.get('#form-validate > .actions-toolbar > div.primary > .action').click();





    });






});