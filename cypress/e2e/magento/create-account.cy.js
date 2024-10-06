describe("Test Create Account Magento", () => {
    beforeEach(() => {
      cy.visit(
        "https://magento.softwaretestingboard.com/customer/account/create/"
      );
    });
  
    it("Create a new customer account", () => {
        cy.visit("https://magento.softwaretestingboard.com/customer/account/create/");
        cy.get("#firstname").type("rayhan");
        cy.get("#lastname").type("gerry");
        cy.get('#email_address').type("rayhangerry22@yahoo.com");
        cy.get("#password").type("Bajubaru22");
        cy.get('#password-confirmation').type("Bajubaru22");
        cy.get('#form-validate > .actions-toolbar > div.primary > .action').click();
        cy.get('.message-success').should("be.visible");
        cy.get('.message-success > div').should("contain.text","Thank you for registering with Main Website Store.");
        });


    });
