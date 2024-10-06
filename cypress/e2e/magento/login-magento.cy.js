describe("Test Login Magento", () => {
    beforeEach(() => {
      cy.visit(
        "https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/"
      );
    });

    it("Test Wrong Email ", () => {
        cy.get('[name="login[username]"]').type("Akram@yaho.com");
        cy.get('[name="login[password]"]').type("bajubaru22");
        cy.get("#send2").click();
        cy.url().should("include", "https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/");
        cy.get(".message-error").should(
            "contain.text",
            "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."
        );
    });


    it("Test failed Success", () => {
        cy.get('[name="login[username]"]').type("akram@yahoo.com");
        cy.get('[name="login[password]"]').type("bajubaru22");
        cy.get("#send2").click();
        cy.url().should("include", "https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/");
        cy.get(".message-error").should(
            "contain.text",
            "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."
        );
    });
    
    it("Test Login Success", () => {
        cy.get('[name="login[username]"]').type("akram@yahoo.com");
        cy.get('[name="login[password]"]').type("Bajubaru22");
        cy.get("#send2").click();
        cy.url().should("include", "https://magento.softwaretestingboard.com/");
    });


    




});
  