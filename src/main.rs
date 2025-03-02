use multiversx_sc::imports::*;
use multiversx_sc::derive_imports::*;

#[multiversx_sc::contract]
pub trait RewardContract {
    #[init]
    fn init(&self) {}

    #[endpoint]
    fn send_reward(&self, to: ManagedAddress, amount: BigUint) {
        require!(amount > 0, "Ödül miktarı 0'dan büyük olmalı");
        self.send().direct(&to, &TokenIdentifier::egld(), 0, &amount);
    }
}
